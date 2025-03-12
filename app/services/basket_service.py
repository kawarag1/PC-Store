from app.models.models import Basket as Basket_Table, User
from app.schemas.request import basket_schema
from app.schemas.request.basket_schema import Basket
from app.schemas.request.product import Product as ProductRequest
from app.database.connector import *
from app.schemas.response.goods import Goods


from fastapi import Depends, HTTPException
from sqlalchemy import select
from typing import List



class BasketService():
    def __init__(self, session:Session):
        self.session = session

    async def check_basket(self, user_id : int) -> List[Basket]:
        query = select(Basket_Table).filter(Basket_Table.user_id == user_id)

        result = self.session.execute(query)
        basket = result.scalars().all()
        if basket is None:
            raise HTTPException(
                status_code = 404,
                detail = "Ваша корзина пуста"
            )
        return basket
        
    

    async def add_to_basket(self, data: ProductRequest, user_id: int):
        if "CPU" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "GPU" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "RAM" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "CASE" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "M2" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "SSD" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "HDD" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "MB" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "VENT" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "TOWER" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        elif "PU" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket_Table)
        
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()



    async def basket_clear(self, user_id: int):
        query = delete(Basket_Table).filter(Basket_Table.user_id == user_id)

        self.session.execute(query)
        self.session.commit()
        
    
    