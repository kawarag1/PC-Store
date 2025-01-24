from app.database.connector import get_session
from app.models.models import User
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


@router.post("/create_order")
async def create_order(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    result = await OrderService(session).create_order(user.id)
    return result