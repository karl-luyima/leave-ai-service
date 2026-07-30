from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.leave_graph import build_leave_graph
from app.providers.checkinpro_provider import CheckinProProvider


router = APIRouter(
    prefix="/leave",
    tags=["Leave AI"]
)


provider = CheckinProProvider()

leave_graph = build_leave_graph(
    provider
)


class LeaveRequest(BaseModel):

    leave_type: str

    days_requested: int

    reason: str



@router.post("/evaluate")
def evaluate_leave(
    request: LeaveRequest
):

    result = leave_graph.invoke(
        {
            "employee_id": None,

            "leave_request": request.dict(),

            "observation": None,

            "reasoning": None,

            "risk": None,

            "decision": None,

            "action": None
        }
    )


    return result