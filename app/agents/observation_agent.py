class ObservationAgent:


    def __init__(
        self,
        provider
    ):

        self.provider = provider



    def observe(
        self,
        leave_request=None
    ):

        employee = self.provider.get_employee()

        leaves = self.provider.get_leave_history()

        policies = self.provider.get_policy()


        if not employee:

            return {
                "error": "Employee not found"
            }



        pending = [
            leave
            for leave in leaves
            if leave["status"] == "Pending"
        ]



        approved_days = sum(
            int(leave["total_leave_days"])
            for leave in leaves
            if leave["status"] == "Approved"
        )



        return {

            "employee": employee,


            "leave_request": leave_request,


            "leave_summary": {

                "total_requests": len(leaves),

                "pending_requests": len(pending),

                "approved_days": approved_days

            },


            "leave_history": leaves,


            "policies": policies

        }