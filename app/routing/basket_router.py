from app.database.connector import get_session
from app.models.models import User
from app.schemas.request.basket_schema import Basket
from app.schemas.request.product import Product as ProductRequest
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
async def add_to_basket(request: ProductRequest, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    result = await BasketService(session).add_to_basket(request, user.id)
    return result


@router.delete("/clear_all_basket")
async def clear_all_basket(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    result = await BasketService(session).basket_clear(user.id)
    return result


@router.delete("/delete_one_from_basket")
async def delete_one_from_basket(data: ProductRequest, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    result = await BasketService(session).delete_one_from_basket(user.id, data)
    return result