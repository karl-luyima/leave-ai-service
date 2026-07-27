from fastapi import APIRouter
from pydantic import BaseModel

from app.core.logger import logger
from app.core.exceptions import LeaveAIException

from app.workflow.leave_graph import build_leave_graph
from app.agents.reminder_agent import LeaveReminderAgent



router = APIRouter(
    prefix="/leave",
    tags=["Leave AI"]
)


graph = build_leave_graph()

reminder_agent = LeaveReminderAgent()



class LeaveRequest(BaseModel):

    employee_id: int

    days_requested: int



class LeaveDecisionResponse(BaseModel):

    employee_id: int

    employee: str | None = None

    approved: bool

    recommendation: str

    confidence: int

    explanation: str | None = None



@router.post(
    "/analyze",
    response_model=LeaveDecisionResponse
)
def analyze_leave(
    request: LeaveRequest
):

    logger.info(
        f"Leave request received: employee={request.employee_id}, days={request.days_requested}"
    )


    try:

        result = graph.invoke(
            {
                "employee_id": request.employee_id,
                "days_requested": request.days_requested
            }
        )


        if not result.get("final_decision"):

            raise LeaveAIException(
                "No decision was generated for this leave request"
            )


        logger.info(
            f"Decision generated: {result['final_decision']['recommendation']}"
        )


        return result["final_decision"]



    except LeaveAIException:

        raise



    except Exception as e:

        logger.error(
            f"Leave analysis failed: {str(e)}"
        )


        raise LeaveAIException(
            "Unable to process leave request"
        )



@router.get(
    "/reminders"
)
def get_leave_reminders():

    logger.info(
        "Leave reminder request received"
    )


    try:

        reminders = reminder_agent.analyze_leave_usage()


        logger.info(
            f"Generated {len(reminders)} leave reminders"
        )


        return {
            "reminders": reminders
        }



    except Exception as e:

        logger.error(
            f"Reminder generation failed: {str(e)}"
        )


        raise LeaveAIException(
            "Unable to generate leave reminders"
        )