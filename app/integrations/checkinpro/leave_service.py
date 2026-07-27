from app.integrations.checkinpro.client import CheckinProClient



class LeaveService:


    def __init__(self):

        self.client = CheckinProClient()



    def get_leave_history(
        self,
        employee_id
    ):

        return self.client.get(
            f"/employees/{employee_id}/leave-history"
        )