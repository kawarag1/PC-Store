from app.models.models import Basket as Basket_Table, User
from app.schemas.request.basket_schema import Basket
from app.database.connector import *

from fastapi import Depends, HTTPException
from sqlalchemy import select

from app.security.jwtmanager import get_current_user


class BasketService():
    def __init__(self, session:Session):
        self.session = session

    async def check_basket(self, user_id : int):
        query = select(Basket_Table).filter(Basket_Table.user_id == user_id)

        result = self.session.execute(query)
        basket = result.scalars().all()
        if basket is None:
            raise HTTPException(
                status_code = 404,
                detail = "Ваша корзина пуста"
            )
        return basket
    

    async def add_to_basket(self, data: Basket_Table, user_id: int):
        data.user_id = user_id
        query = insert(Basket_Table).values(data).returning(Basket)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()
        
    