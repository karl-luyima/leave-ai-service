class ObservationAgent:


    def __init__(
        self,
        provider
    ):

        self.provider = provider



    def observe(
        self,
        leave_request
    ):


        employee = self.provider.get_employee()



        history = self.provider.get_leave_history()



        policies = self.provider.get_policy()



        pending_requests = [

            leave

            for leave in history

            if leave.get(
                "status"
            ) == "Pending"

        ]



        approved_days = sum(

            int(
                leave.get(
                    "total_leave_days",
                    0
                )
            )

            for leave in history

            if leave.get(
                "status"
            ) in [
                "Approved",
                "Approve"
            ]

        )



        return {


            "employee": employee,


            "leave_request": leave_request,


            "leave_summary": {


                "total_requests": len(
                    history
                ),


                "pending_requests": len(
                    pending_requests
                ),


                "approved_days": approved_days

            },


            "leave_history": history,


            "policies": policies

        }