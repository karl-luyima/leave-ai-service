from fastapi import FastAPI, Header, HTTPException


app = FastAPI(
    title="Mock CheckinPro API"
)



def verify_token(
    authorization
):

    if authorization != "Bearer dummy_key":

        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )



@app.get(
    "/employees/{employee_id}"
)
def get_employee(
    employee_id: int,
    authorization: str = Header(None)
):

    verify_token(
        authorization
    )


    return {

        "id": employee_id,

        "name": "John Doe",

        "department": "IT",

        "leave_balance": 20

    }



@app.get(
    "/employees/{employee_id}/leave-history"
)
def get_leave_history(
    employee_id: int,
    authorization: str = Header(None)
):

    verify_token(
        authorization
    )


    return [

        {
            "year": 2026,
            "days_taken": 5
        }

    ]



@app.get(
    "/employees/{employee_id}/attendance"
)
def get_attendance(
    employee_id: int,
    authorization: str = Header(None)
):

    verify_token(
        authorization
    )


    return {

        "attendance_rate": 96,

        "late_days": 0

    }