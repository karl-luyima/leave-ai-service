from app.integrations.checkinpro.client import CheckinProClient


class LeaveService:


    def __init__(self):

        self.client = CheckinProClient()



    def get_leave_data(self):

        response = self.client.post(
            "/getEmployeeLeavesData",
            {
                "username": self.client.username,
                "password": self.client.password,
                "companyEmail": self.client.company_email
            }
        )


        if not response:
            return None


        if response.get("status") != "SUCCESS":
            return None


        return response["data"]



    def get_leave_history(
        self,
        employee_id=None
    ):

        data = self.get_leave_data()


        if not data:
            return []


        return data.get(
            "leaves",
            []
        )



    def get_leave_types(self):

        data = self.get_leave_data()


        if not data:
            return []


        return data.get(
            "leave_types",
            []
        )