from langgraph.graph import StateGraph, END

from app.graph.state import LeaveState

from app.agents.observation_agent import ObservationAgent
from app.agents.reasoning_agent import ReasoningAgent
from app.agents.risk_assessment import RiskAssessmentAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.action_agent import ActionAgent

from app.agents.risk_engine import LeaveRiskEngine



def build_leave_graph(provider):


    observation_agent = ObservationAgent(
        provider
    )

    reasoning_agent = ReasoningAgent()


    risk_engine = LeaveRiskEngine()

    risk_agent = RiskAssessmentAgent(
        risk_engine
    )


    decision_agent = DecisionAgent()

    action_agent = ActionAgent()



    graph = StateGraph(
        LeaveState
    )



    def observation_node(state):

        result = observation_agent.observe(
            state["leave_request"]
        )

        return {
            "observation": result
            "employee_id": result["employee"]["employee_id"]
        }



    def reasoning_node(state):

        result = reasoning_agent.analyze(
            state["observation"]
        )

        return {
            "reasoning": result
        }



    def risk_node(state):

        result = risk_agent.assess(
            {
                **state["observation"],
                **state["reasoning"]
            }
        )

        return {
            "risk": result
        }



    def decision_node(state):

        result = decision_agent.decide(
            {
                **state["reasoning"],
                "risk": state["risk"]
            }
        )

        return {
            "decision": result
        }



    def action_node(state):

        result = action_agent.execute(
            state["decision"]
        )

        return {
            "action": result
        }



    graph.add_node(
        "observation",
        observation_node
    )


    graph.add_node(
        "reasoning",
        reasoning_node
    )


    graph.add_node(
        "risk",
        risk_node
    )


    graph.add_node(
        "decision",
        decision_node
    )


    graph.add_node(
        "action",
        action_node
    )



    graph.set_entry_point(
        "observation"
    )



    graph.add_edge(
        "observation",
        "reasoning"
    )


    graph.add_edge(
        "reasoning",
        "risk"
    )


    graph.add_edge(
        "risk",
        "decision"
    )


    graph.add_edge(
        "decision",
        "action"
    )


    graph.add_edge(
        "action",
        END
    )


    return graph.compile()