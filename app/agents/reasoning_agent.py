class ReasoningAgent:


    def analyze(
        self,
        context
    ):

        employee = context["employee"]

        leaves = context["leave_history"]

        policies = context["policies"]

        leave_request = context.get(
            "leave_request"
        )


        observations = []


        # Check existing pending requests
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



        # Analyse previous leave history
        for leave in leaves:

            leave_days = int(
                leave.get(
                    "total_leave_days",
                    0
                )
            )


            observations.append(
                f"Previous leave request of {leave_days} days is currently {leave['status']}."
            )



        # Analyse new leave request
        if leave_request:

            requested_type = leave_request["leave_type"]

            requested_days = leave_request["days_requested"]


            allowed_days = policies.get(
                requested_type,
                0
            )


            if allowed_days == 0:

                observations.append(
                    f"Leave type '{requested_type}' was not found in company policy."
                )


            elif requested_days > allowed_days:

                observations.append(
                    f"Requested {requested_days} days exceeds the allowed {allowed_days} days for {requested_type}."
                )


            else:

                observations.append(
                    f"Requested {requested_days} days is within the allowed {allowed_days} days for {requested_type}."
                )



        return {

            "employee": employee,

            "leave_request": leave_request,

            "leave_history": leaves,

            "policies": policies,

            "observations": observations,

            "analysis": (
                "Leave request analysed against "
                "employee history and company policies."
            )

        }