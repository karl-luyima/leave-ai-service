from app.integrations.checkinpro.client import CheckinProClient


class EmployeeService:


    def __init__(self):

        self.client = CheckinProClient()



    def get_employee(
        self,
        employee_id
    ):

        data = self.client.get(
            f"/employees/{employee_id}"
        )


        return {

            "id": data["id"],

            "name": data["name"],

            "department": data["department"],

            "leave_balance": data["leave_balance"]

        }