class ActionAgent:


    def execute(
        self,
        decision
    ):


        action = None


        if decision["decision"] == "APPROVE":

            action = (
                "Notify HR that leave can proceed."
            )


        elif decision["decision"] == "REVIEW":

            action = (
                "Escalate request to HR for review."
            )


        else:

            action = (
                "Reject request and notify employee."
            )


        return {

            "decision":
                decision["decision"],

            "confidence":
                decision["confidence"],

            "action":
                action

        }