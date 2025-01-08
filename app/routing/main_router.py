from fastapi import APIRouter
from app.routing.user_router import router as user_router

main_router = APIRouter(
    prefix="/v1"
)


main_router.include_router(user_router)