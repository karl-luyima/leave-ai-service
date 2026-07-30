from fastapi import FastAPI

from app.api.leave_routes import router


app = FastAPI(
    title="Leave AI Service",
    description="Agentic AI leave decision service"
)


app.include_router(
    router
)