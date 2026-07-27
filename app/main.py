from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.leave_routes import router as leave_router
from app.core.exceptions import LeaveAIException
from app.core.logger import logger

from app.scheduler.leave_scheduler import scheduler


app = FastAPI(
    title="Leave AI Service",
    version="1.0"
)


@app.on_event("startup")
def start_scheduler():

    if not scheduler.running:
        scheduler.start()

    logger.info(
        "Leave Reminder Scheduler started"
    )



@app.on_event("shutdown")
def stop_scheduler():

    scheduler.shutdown()

    logger.info(
        "Leave Reminder Scheduler stopped"
    )



app.include_router(
    leave_router
)