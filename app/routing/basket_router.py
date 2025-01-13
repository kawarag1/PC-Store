from app.database.connector import get_session
from app.services.basket_service import BasketService


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = "/basket"
)

@router.get("/check")
async def check(user_id: int, session: Session = Depends(get_session)):
    result = await BasketService(session).check_basket(user_id)
    return result