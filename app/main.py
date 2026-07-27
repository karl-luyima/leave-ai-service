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


# Start scheduler when FastAPI starts
@app.on_event("startup")
def start_scheduler():

    if not scheduler.running:
        scheduler.start()

    logger.info(
        "Leave Reminder Scheduler started"
    )


# Stop scheduler when FastAPI shuts down
@app.on_event("shutdown")
def stop_scheduler():

    if scheduler.running:
        scheduler.shutdown()

    logger.info(
        "Leave Reminder Scheduler stopped"
    )


# Register API routes
app.include_router(
    leave_router
)


# Custom Leave AI exception handler
@app.exception_handler(LeaveAIException)
async def leave_ai_exception_handler(
    request: Request,
    exc: LeaveAIException
):

    logger.error(
        f"Leave AI error: {exc.message}"
    )

    return JSONResponse(
        status_code=400,
        content={
            "error": "Leave AI processing failed",
            "message": exc.message
        }
    )


# General exception handler
@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        f"Unexpected error: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred"
        }
    )


# Root endpoint
@app.get("/")
def home():

    return {
        "service": "Leave AI Service",
        "status": "running"
    }


# Health check endpoint
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "leave-ai-service"
    }