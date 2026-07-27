import json
import random
from datetime import datetime, timedelta
from pathlib import Path


BASE_DIR = Path(__file__).parent


departments = [
    "Finance",
    "Information Technology",
    "Human Resources",
    "Marketing",
    "Operations",
    "Sales",
    "Legal",
    "Procurement",
    "Customer Support",
    "Administration"
]


positions = {
    "Finance": [
        "Accountant",
        "Financial Analyst",
        "Finance Manager"
    ],

    "Information Technology": [
        "Software Engineer",
        "System Administrator",
        "Data Analyst"
    ],

    "Human Resources": [
        "HR Officer",
        "Recruiter"
    ],

    "Marketing": [
        "Marketing Specialist",
        "Content Manager"
    ],

    "Operations": [
        "Operations Officer",
        "Operations Manager"
    ],

    "Sales": [
        "Sales Executive",
        "Sales Manager"
    ],

    "Legal": [
        "Legal Officer"
    ],

    "Procurement": [
        "Procurement Officer"
    ],

    "Customer Support": [
        "Support Agent"
    ],

    "Administration": [
        "Administrator"
    ]
}


names = [
    "John",
    "Sarah",
    "Michael",
    "Emily",
    "David",
    "Daniel",
    "Grace",
    "Robert",
    "Linda",
    "James",
    "Peter",
    "Mary",
    "William",
    "Anna",
    "George"
]


surnames = [
    "Smith",
    "Johnson",
    "Brown",
    "Williams",
    "Jones",
    "Taylor",
    "Davis",
    "Wilson",
    "Anderson",
    "Thomas"
]


def random_date(start, end):

    difference = end - start

    days = random.randint(
        0,
        difference.days
    )

    return (
        start + timedelta(days=days)
    ).strftime("%Y-%m-%d")


# ---------------------------
# Employees
# ---------------------------

employees = []

for i in range(1,101):

    department = random.choice(departments)

    employees.append({

        "employee_id": 1000+i,

        "name":
            random.choice(names)
            + " "
            + random.choice(surnames),

        "department": department,

        "position":
            random.choice(
                positions[department]
            ),

        "manager_id":
            random.randint(200,215),

        "employment_type":
            random.choice(
                [
                    "Permanent",
                    "Contract"
                ]
            ),

        "hire_date":
            random_date(
                datetime(2020,1,1),
                datetime(2025,1,1)
            ),

        "leave_balance":
            random.randint(0,21),

        "annual_entitlement":
            21,

        "sick_leave_balance":
            random.randint(0,10),

        "status":
            "Active"

    })


# ---------------------------
# Leave History
# ---------------------------

leave_history=[]

leave_types=[
    "Annual",
    "Sick",
    "Emergency",
    "Maternity",
    "Study"
]


for i in range(1000):

    employee=random.choice(employees)

    days=random.randint(1,10)

    start=datetime(2024,1,1)

    leave_history.append({

        "leave_id":i+1,

        "employee_id":
            employee["employee_id"],

        "leave_type":
            random.choice(leave_types),

        "start_date":
            random_date(
                start,
                datetime.now()
            ),

        "days":
            days,

        "status":
            random.choice(
                [
                    "Approved",
                    "Rejected",
                    "Cancelled"
                ]
            )
    })


# ---------------------------
# Leave Requests
# ---------------------------

requests=[]


for i in range(150):

    employee=random.choice(employees)

    requests.append({

        "request_id":i+1,

        "employee_id":
            employee["employee_id"],

        "requested_days":
            random.randint(1,15),

        "reason":
            random.choice(
                [
                    "Vacation",
                    "Family event",
                    "Medical",
                    "Personal"
                ]
            ),

        "status":
            random.choice(
                [
                    "Pending",
                    "Approved",
                    "Rejected"
                ]
            )

    })



# ---------------------------
# Attendance
# ---------------------------

attendance=[]


for employee in employees:

    attendance.append({

        "employee_id":
            employee["employee_id"],

        "late_days":
            random.randint(0,10),

        "absent_days":
            random.randint(0,5),

        "attendance_rate":
            round(
                random.uniform(
                    85,
                    100
                ),
                2
            )
    })



# ---------------------------
# Departments
# ---------------------------

department_data=[]


for dep in departments:

    department_data.append({

        "department":dep,

        "minimum_staff":
            random.randint(3,8),

        "current_staff":
            random.randint(8,20)

    })



# ---------------------------
# Policies
# ---------------------------

policies={

    "annual_leave_days":21,

    "carry_forward_limit":5,

    "minimum_notice_days":7,

    "maximum_consecutive_days":15,

    "approval_rules":{

        "less_than_10_days":
            "Manager",

        "10_days_or_more":
            "HR"
    },

    "team_availability_threshold":
        60

}



# ---------------------------
# Holidays
# ---------------------------

holidays=[

    {
        "name":"New Year",
        "date":"2026-01-01"
    },

    {
        "name":"Christmas",
        "date":"2026-12-25"
    }

]



def save(filename,data):

    with open(
        BASE_DIR / filename,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



save(
    "employees.json",
    employees
)

save(
    "leave_history.json",
    leave_history
)

save(
    "leave_requests.json",
    requests
)

save(
    "attendance.json",
    attendance
)

save(
    "departments.json",
    department_data
)

save(
    "policies.json",
    policies
)

save(
    "holidays.json",
    holidays
)


print("Dummy HR dataset generated successfully")