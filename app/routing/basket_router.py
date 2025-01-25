from app.database.connector import get_session
from app.models.models import User
from app.schemas.request.basket_schema import Basket
from app.security.jwtmanager import get_current_user
from app.services.basket_service import BasketService


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



router = APIRouter(
    prefix = "/basket"
)

@router.get("/check")
async def check(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    result = await BasketService(session).check_basket(user.id)
    return result

@router.post("/add_to_basket")
async def add_to_basket(request: Basket, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    result = await BasketService(session).add_to_basket(user.id, request)
    return result