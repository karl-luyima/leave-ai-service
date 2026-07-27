from sqlalchemy import Column, Integer, String, Float

from app.database.connection import Base



class Employee(Base):

    __tablename__ = "employees"


    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    department = Column(
        String
    )

    leave_balance = Column(
        Integer
    )



class LeaveHistory(Base):

    __tablename__ = "leave_history"


    id = Column(
        Integer,
        primary_key=True
    )

    employee_id = Column(
        Integer
    )

    year = Column(
        Integer
    )

    days_taken = Column(
        Integer
    )



class Attendance(Base):

    __tablename__ = "attendance"


    id = Column(
        Integer,
        primary_key=True
    )

    employee_id = Column(
        Integer
    )

    attendance_rate = Column(
        Float
    )

    late_days = Column(
        Integer
    )