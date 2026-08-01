from app.providers.interface import LeaveDataProvider

from app.integrations.checkinpro.leave_service import LeaveService



class CheckinProProvider(LeaveDataProvider):


    def __init__(self):

        self.leave_service = LeaveService()



    def _get_data(self):

        response = self.leave_service.get_leave_data()


        if not response:

            return None



        return response.get(
            "data",
            {}
        )



    def get_employee(
        self,
        employee_id=None
    ):

        data = self._get_data()


        if not data:

            return None



        employee = {

            "employee_id": data.get(
                "employee_id"
            ),

            "name": data.get(
                "name"
            )

        }



        return employee



    def get_leave_history(
        self,
        employee_id=None
    ):

        data = self._get_data()


        if not data:

            return []



        return data.get(
            "leaves",
            []
        )



    def get_leave_requests(
        self,
        employee_id=None
    ):

        leaves = self.get_leave_history(
            employee_id
        )


        return [

            leave

            for leave in leaves

            if leave.get(
                "status"
            ) == "Pending"

        ]



    def get_leave_types(
        self
    ):

        data = self._get_data()


        if not data:

            return []



        return data.get(
            "leave_types",
            []
        )



    def get_policy(
        self
    ):

        leave_types = self.get_leave_types()


        policies = {}



        for leave_type in leave_types:

            policies[
                leave_type["title"]
            ] = leave_type["days"]



        return policies



    def get_leave_balance(
        self
    ):

        employee = self.get_employee()


        policies = self.get_policy()


        history = self.get_leave_history()



        used_leave = {}



        for leave in history:

            if leave.get("status") in [
                "Approved",
                "Approve"
            ]:

                leave_type_id = leave.get(
                    "leave_type_id"
                )


                days = int(
                    leave.get(
                        "total_leave_days",
                        0
                    )
                )


                used_leave[leave_type_id] = (

                    used_leave.get(
                        leave_type_id,
                        0
                    )

                    +

                    days

                )



        return {

            "employee": employee,

            "policies": policies,

            "used_leave": used_leave

        }



    def get_attendance(
        self,
        employee_id=None
    ):

        return None



    def get_department(
        self,
        department=None
    ):

        return None