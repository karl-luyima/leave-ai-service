from app.providers.interface import LeaveDataProvider

from app.database.connection import SessionLocal
from app.database.models import (
    Employee,
    LeaveHistory,
    Attendance
)


class DatabaseLeaveProvider(
    LeaveDataProvider
):


    def __init__(self):

        self.db = SessionLocal()



    def get_employee(
        self,
        employee_id
    ):

        employee = (
            self.db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )


        if not employee:
            return None


        return {
            "id": employee.id,
            "name": employee.name,
            "department": employee.department,
            "leave_balance": employee.leave_balance
        }



    def get_all_employees(
        self
    ):

        employees = (
            self.db.query(Employee)
            .all()
        )


        return [
            {
                "id": employee.id,
                "name": employee.name,
                "department": employee.department,
                "leave_balance": employee.leave_balance
            }

            for employee in employees
        ]



    def get_leave_history(
        self,
        employee_id
    ):

        records = (
            self.db.query(LeaveHistory)
            .filter(
                LeaveHistory.employee_id == employee_id
            )
            .all()
        )


        return [
            {
                "year": r.year,
                "days_taken": r.days_taken
            }
            for r in records
        ]



    def get_attendance(
        self,
        employee_id
    ):

        record = (
            self.db.query(Attendance)
            .filter(
                Attendance.employee_id == employee_id
            )
            .first()
        )


        if not record:

            return {
                "attendance_rate": 0,
                "late_days": 0
            }


        return {
            "attendance_rate": record.attendance_rate,
            "late_days": record.late_days
        }



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

        return []



    def get_policy(
        self
    ):

        return {
            "max_consecutive_days": 30
        }
