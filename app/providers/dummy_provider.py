from .interface import LeaveDataProvider


class DummyLeaveProvider(LeaveDataProvider):

    def get_employee(self, employee_id):

        employees = [
            {
                "id": 1,
                "name": "John Doe",
                "department": "Finance",
                "leave_balance": 18
            },
            {
                "id": 2,
                "name": "Mary Smith",
                "department": "IT",
                "leave_balance": 5
            }
        ]

        for employee in employees:
            if employee["id"] == employee_id:
                return employee

        return None


    def get_leave_requests(self, employee_id):
        return [
            {
                "employee_id": employee_id,
                "type": "Annual Leave",
                "days": 5,
                "status": "Approved"
            }
        ]


    def get_leave_history(self, employee_id):
        return [
            {
                "year": 2025,
                "days_taken": 12
            },
            {
                "year": 2026,
                "days_taken": 3
            }
        ]


    def get_attendance(self, employee_id):
        return {
            "attendance_rate": 95,
            "late_days": 1
        }


    def get_department(self, employee_id):
        employee = self.get_employee(employee_id)

        if employee:
            return employee["department"]

        return None


    def get_policy(self):
        return {
            "max_consecutive_days": 30,
            "minimum_notice_days": 3
        }