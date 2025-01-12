from fastapi import APIRouter
from app.routing.user_router import router as user_router
from app.routing.basket_router import router as basket_router

main_router = APIRouter(
    prefix="/v1"
)


main_router.include_router(user_router)
main_router.include_router(basket_router)