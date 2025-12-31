from fastapi import APIRouter
from app.api.routes import generate_route, health_route


api_router = APIRouter()

api_router.include_router(generate_route.router, prefix="/generate", tags=["Generate"])
api_router.include_router(health_route.router, prefix="/health", tags=["Health"])