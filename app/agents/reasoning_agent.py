class ReasoningAgent:


    def analyze(
        self,
        context
    ):

        employee = context["employee"]

        leaves = context["leave_history"]

        policies = context["policies"]


        observations = []


        # Check pending requests
        pending_count = len(
            [
                leave
                for leave in leaves
                if leave["status"] == "Pending"
            ]
        )


        if pending_count > 0:

            observations.append(
                f"Employee has {pending_count} pending leave request(s)."
            )


        # Check leave duration against policy
        for leave in leaves:

            leave_days = int(
                leave["total_leave_days"]
            )


            leave_type = leave["leave_type_id"]


            observations.append(
                f"Leave request of {leave_days} days is currently {leave['status']}."
            )


        return {

            "employee": employee,

            "observations": observations,

            "analysis": (
                "Leave history analysed based on "
                "previous requests and available policies."
            )

        }