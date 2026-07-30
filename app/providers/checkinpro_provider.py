from app.providers.interface import LeaveDataProvider

from app.integrations.checkinpro.leave_service import LeaveService



class CheckinProProvider(LeaveDataProvider):


    def __init__(self):

        self.leave_service = LeaveService()



    def get_employee(self):

        data = self.leave_service.get_leave_data()


        if not data:

            return None



        return {

            "employee_id": data["employee_id"],

            "name": data["name"]

        }



    def get_leave_history(self):

        data = self.leave_service.get_leave_data()


        if not data:

            return []



        return data.get(
            "leaves",
            []
        )



    def get_leave_types(self):

        data = self.leave_service.get_leave_data()


        if not data:

            return []



        return data.get(
            "leave_types",
            []
        )



    def get_attendance(self):

        return None



    def get_department(self):

        return None



    def get_leave_requests(self):

        data = self.leave_service.get_leave_data()


        if not data:

            return []



        return [
            leave
            for leave in data.get("leaves", [])
            if leave["status"] == "Pending"
        ]



    def get_policy(self):

        data = self.leave_service.get_leave_data()


        if not data:

            return {}



        policies = {}



        for leave_type in data.get("leave_types", []):

            policies[
                leave_type["title"]
            ] = leave_type["days"]



        return policies