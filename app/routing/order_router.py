from app.database.connector import get_session
from app.models.models import User
from app.schemas.request.order_schema import Order as OrderClass
from app.schemas.request.product import Product as ProductRequest
from app.security.jwtmanager import get_current_user
from app.services.order_service import OrderService


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = "/order"
)

@router.get("/check")
async def check(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    result = await OrderService(session).check_orders(user.id)
    return result


@router.post("/create_fast_order")
async def create_order(order: ProductRequest, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    result = await OrderService(session).create_fast_order(order, user.id)
    return result