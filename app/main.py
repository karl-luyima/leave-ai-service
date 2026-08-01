from fastapi import FastAPI

from app.api.leave_routes import router

from app.api.reminder_routes import router as reminder_router



app = FastAPI(
    title="Leave AI Service",
    description="Agentic AI leave decision and reminder service"
)



# Leave evaluation endpoint
app.include_router(
    router
)



# Leave reminder endpoint
app.include_router(
    reminder_router
)