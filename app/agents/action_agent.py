class ActionAgent:


    def execute(
        self,
        decision
    ):


        decision_type = decision["decision"]


        if decision_type == "APPROVE":

            return {

                "decision": decision_type,

                "confidence": decision["confidence"],

                "action": "Approve leave request.",

                "notification": (
                    "Notify HR and employee that the leave request "
                    "has been approved."
                )

            }


        elif decision_type == "REVIEW":

            return {

                "decision": decision_type,

                "confidence": decision["confidence"],

                "action": "Send request for HR review.",

                "notification": (
                    "Notify HR that this leave request requires "
                    "manual review."
                )

            }


        else:

            return {

                "decision": decision_type,

                "confidence": decision["confidence"],

                "action": "Reject leave request.",

                "notification": (
                    "Notify employee that the leave request "
                    "does not meet leave policy requirements."
                )

            }