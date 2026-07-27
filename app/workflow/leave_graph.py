from typing import TypedDict, Optional

from langgraph.graph import StateGraph, END

from app.providers.database_provider import DatabaseLeaveProvider
from app.providers.checkinpro_provider import CheckinProProvider

from app.config import DATA_PROVIDER

from app.agents.policy_engine import LeavePolicyEngine
from app.agents.risk_engine import LeaveRiskEngine
from app.agents.confidence_engine import ConfidenceEngine

from app.llm.reasoning import generate_explanation
from app.memory.decision_memory import save_decision



class LeaveState(TypedDict):

    employee_id: int
    days_requested: int

    employee: Optional[dict]

    attendance: dict
    history: list

    evaluation: dict

    risk: dict

    confidence: dict

    explanation: str

    final_decision: dict



# -------------------------
# Services
# -------------------------

if DATA_PROVIDER == "checkinpro":

    provider = CheckinProProvider()

else:

    provider = DatabaseLeaveProvider()



policy_engine = LeavePolicyEngine()

risk_engine = LeaveRiskEngine()

confidence_engine = ConfidenceEngine()



# -------------------------
# Nodes
# -------------------------


def load_employee(state):

    employee = provider.get_employee(
        state["employee_id"]
    )

    state["employee"] = employee

    return state



def check_employee_exists(state):

    if not state.get("employee"):

        return "employee_not_found"


    return "continue"




def employee_not_found(state):

    state["final_decision"] = {

        "employee_id": state["employee_id"],

        "approved": False,

        "recommendation": "REJECT",

        "confidence": 0,

        "reason": "Employee not found"

    }


    return state




def analyze_history(state):

    history = provider.get_leave_history(
        state["employee_id"]
    )

    state["history"] = history

    return state




def analyze_attendance(state):

    attendance = provider.get_attendance(
        state["employee_id"]
    )

    state["attendance"] = attendance

    return state




def evaluate_policy(state):

    evaluation = policy_engine.evaluate(
        state["employee"],
        state["attendance"],
        state["history"],
        state["days_requested"]
    )

    state["evaluation"] = evaluation

    return state




def analyze_risk(state):

    risk = risk_engine.analyze(
        state["employee"],
        state["attendance"],
        state["history"],
        state["days_requested"]
    )

    state["risk"] = risk

    return state




def calculate_confidence(state):

    confidence = confidence_engine.calculate(
        state["evaluation"]["score"],
        state["risk"]["risk_score"]
    )

    state["confidence"] = confidence

    return state




def generate_decision_explanation(state):

    decision = {

        "employee_id": state["employee_id"],

        "employee": state["employee"]["name"],

        "days_requested": state["days_requested"],

        "approved": state["evaluation"]["approved"],

        "policy_score": state["evaluation"]["score"],

        "risk_score": state["risk"]["risk_score"],

        "confidence": state["confidence"]["confidence"],

        "recommendation": state["confidence"]["recommendation"],

        "risks": state["risk"]["risks"],

        "reasons": state["evaluation"]["reasons"]

    }


    explanation = generate_explanation(
        decision
    )


    decision["explanation"] = explanation


    state["explanation"] = explanation

    state["final_decision"] = decision


    return state




def save_memory(state):

    save_decision(
        state["final_decision"]
    )

    return state




# -------------------------
# Graph
# -------------------------


def build_leave_graph():

    graph = StateGraph(
        LeaveState
    )


    graph.add_node(
        "load_employee",
        load_employee
    )


    graph.add_node(
        "employee_not_found",
        employee_not_found
    )


    graph.add_node(
        "history_analysis",
        analyze_history
    )


    graph.add_node(
        "attendance_analysis",
        analyze_attendance
    )


    graph.add_node(
        "policy_evaluation",
        evaluate_policy
    )


    graph.add_node(
        "risk_analysis",
        analyze_risk
    )


    graph.add_node(
        "confidence",
        calculate_confidence
    )


    graph.add_node(
        "explanation",
        generate_decision_explanation
    )


    graph.add_node(
        "save_memory",
        save_memory
    )


    graph.set_entry_point(
        "load_employee"
    )


    graph.add_conditional_edges(
        "load_employee",
        check_employee_exists,
        {
            "continue": "history_analysis",
            "employee_not_found": "employee_not_found"
        }
    )


    graph.add_edge(
        "employee_not_found",
        END
    )


    graph.add_edge(
        "history_analysis",
        "attendance_analysis"
    )


    graph.add_edge(
        "attendance_analysis",
        "policy_evaluation"
    )


    graph.add_edge(
        "policy_evaluation",
        "risk_analysis"
    )


    graph.add_edge(
        "risk_analysis",
        "confidence"
    )


    graph.add_edge(
        "confidence",
        "explanation"
    )


    graph.add_edge(
        "explanation",
        "save_memory"
    )


    graph.add_edge(
        "save_memory",
        END
    )


    return graph.compile()