from app.providers.dummy_provider import DummyLeaveProvider
from app.agents.policy_engine import LeavePolicyEngine
from app.memory.decision_memory import save_decision
from app.llm.reasoning import generate_explanation


class LeaveAgent:

    def __init__(self):

        self.provider = DummyLeaveProvider()
        self.policy = LeavePolicyEngine()


    def analyze_leave_request(
            self,
            employee_id,
            days_requested
    ):

        employee = self.provider.get_employee(
            employee_id
        )


        if not employee:
            return {
                "approved": False,
                "reason": "Employee not found"
            }


        attendance = self.provider.get_attendance(
            employee_id
        )


        history = self.provider.get_leave_history(
            employee_id
        )


        evaluation = self.policy.evaluate(
            employee,
            attendance,
            history,
            days_requested
        )


        decision = {

            "employee_id": employee_id,

            "employee": employee["name"],

            "days_requested": days_requested,

            "approved": evaluation["approved"],

            "confidence_score": evaluation["score"],

            "reasons": evaluation["reasons"]

        }


        # Generate AI explanation
        decision["explanation"] = generate_explanation(
            decision
        )


        # Store decision in memory
        save_decision(
            decision
        )


        return decision