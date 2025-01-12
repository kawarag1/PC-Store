from app.database.connector import get_session
from app.services.basket_services.basket_check import BasketCheck


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = "/basket"
)

@router.get("/check")
async def check(user_id:int, session:Session = Depends(get_session)):
    result = await BasketCheck(session).check(user_id)
    return result