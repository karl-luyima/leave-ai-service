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
            "data"
        )



    def get_employee(self):

        data = self._get_data()


        if not data:

            return None



        return {

            "employee_id": data.get(
                "employee_id"
            ),

            "name": data.get(
                "name"
            )

        }



    def get_leave_history(self):

        data = self._get_data()


        if not data:

            return []


        return data.get(
            "leaves",
            []
        )



    def get_leave_types(self):

        data = self._get_data()


        if not data:

            return []


        return data.get(
            "leave_types",
            []
        )



    def get_leave_requests(self):

        leaves = self.get_leave_history()


        return [

            leave

            for leave in leaves

            if leave.get("status") == "Pending"

        ]



    def get_policy(self):

        leave_types = self.get_leave_types()


        policies = {}


        for leave_type in leave_types:

            policies[
                leave_type["title"]
            ] = leave_type["days"]


        return policies



    def get_attendance(self):

        return None



    def get_department(self):

        return None