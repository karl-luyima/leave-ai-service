from app.database.connection import SessionLocal

from app.database.models import (
    Employee,
    LeaveHistory,
    Attendance
)



db = SessionLocal()


employee = Employee(
    id=1,
    name="John Doe",
    department="Finance",
    leave_balance=18
)


history = LeaveHistory(
    employee_id=1,
    year=2026,
    days_taken=3
)


attendance = Attendance(
    employee_id=1,
    attendance_rate=95,
    late_days=1
)


db.add(employee)
db.add(history)
db.add(attendance)

db.commit()


print("Seed completed")