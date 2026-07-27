from app.providers.interface import LeaveDataProvider

from app.integrations.checkinpro.employee_service import EmployeeService
from app.integrations.checkinpro.leave_service import LeaveService
from app.integrations.checkinpro.attendance_service import AttendanceService



class CheckinProProvider(
    LeaveDataProvider
):


    def __init__(self):

        self.employee_service = EmployeeService()

        self.leave_service = LeaveService()

        self.attendance_service = AttendanceService()



    def get_employee(
        self,
        employee_id
    ):

        return self.employee_service.get_employee(
            employee_id
        )



    def get_leave_history(
        self,
        employee_id
    ):

        return self.leave_service.get_leave_history(
            employee_id
        )



    def get_attendance(
        self,
        employee_id
    ):

        return self.attendance_service.get_attendance(
            employee_id
        )



    def get_department(
        self,
        employee_id
    ):

        employee = self.get_employee(
            employee_id
        )


        if not employee:
            return None


        return employee["department"]



    def get_leave_requests(
        self,
        employee_id
    ):

        # Future CheckinPro endpoint
        # Example:
        # /employees/{id}/leave-requests

        return []



    def get_policy(self):

        # Future CheckinPro policy endpoint
        # Example:
        # /company/leave-policy

        return {

            "max_consecutive_days": 30,

            "minimum_notice_days": 3

        }