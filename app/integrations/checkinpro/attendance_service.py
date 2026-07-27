from app.integrations.checkinpro.client import CheckinProClient



class AttendanceService:


    def __init__(self):

        self.client = CheckinProClient()



    def get_attendance(
        self,
        employee_id
    ):

        data = self.client.get(
            f"/employees/{employee_id}/attendance"
        )


        return {

            "attendance_rate": data["attendance_rate"],

            "late_days": data["late_days"]

        }