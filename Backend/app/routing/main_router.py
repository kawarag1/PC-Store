from fastapi import APIRouter

from app.routing.user_router import router as user_router
from app.routing.basket_router import router as basket_router
from app.routing.order_router import router as order_router
from app.routing.search_router import router as search_router

main_router = APIRouter(
    prefix="/v1"
)


main_router.include_router(user_router, tags = ["Users"])
main_router.include_router(basket_router, tags = ["Basket"])
main_router.include_router(order_router, tags = ["Orders"])
main_router.include_router(search_router, tags = ["Searching"])