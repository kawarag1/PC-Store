from app.database.connector import get_session
from app.services.order_service import OrderService


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = "/order"
)

@router.get("/check")
async def check(user_id: int, session: Session = Depends(get_session)):
    result = await OrderService(session).check_orders(user_id)
    return result