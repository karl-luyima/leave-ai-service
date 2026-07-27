from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.leave_routes import router as leave_router
from app.core.exceptions import LeaveAIException
from app.core.logger import logger


app = FastAPI(
    title="Leave AI Service",
    version="1.0"
)


app.include_router(
    leave_router
)



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



@app.get("/")
def home():

    return {
        "service": "Leave AI Service",
        "status": "running"
    }



@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "leave-ai-service"
    }