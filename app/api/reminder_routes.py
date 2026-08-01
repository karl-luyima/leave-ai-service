from fastapi import APIRouter, Depends, HTTPException

from app.agents.reminder_agent import LeaveReminderAgent

from app.providers.checkinpro_provider import CheckinProProvider



router = APIRouter(
    prefix="/leave",
    tags=["Leave Reminders"]
)



def get_provider():

    return CheckinProProvider()



@router.get(
    "/reminders"
)
def get_leave_reminders(
    provider: CheckinProProvider = Depends(get_provider)
):


    reminder_agent = LeaveReminderAgent(
        provider
    )


    result = reminder_agent.analyze_leave_usage()



    if not result:

        raise HTTPException(

            status_code=404,

            detail="No reminder data found."

        )



    return result