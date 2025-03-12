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
                gpu_id = data.id
            ).returning(Basket_Table)
        elif "RAM" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                ram_id = data.id
            ).returning(Basket_Table)
        elif "CASE" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                case_id = data.id
            ).returning(Basket_Table)
        elif "M2" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                m2_id = data.id
            ).returning(Basket_Table)
        elif "SSD" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                ssd_id = data.id
            ).returning(Basket_Table)
        elif "HDD" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                hdd_id = data.id
            ).returning(Basket_Table)
        elif "MB" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                motherboard_id = data.id
            ).returning(Basket_Table)
        elif "VENT" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                vent_id = data.id
            ).returning(Basket_Table)
        elif "TOWER" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                cooler_id = data.id
            ).returning(Basket_Table)
        elif "PU" in data.article:
            query = insert(Basket_Table).values(
                user_id = user_id,
                pu_id = data.id
            ).returning(Basket_Table)
        
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()



    async def basket_clear(self, user_id: int):
        query = delete(Basket_Table).filter(Basket_Table.user_id == user_id)

        self.session.execute(query)
        self.session.commit()
        


    async def delete_one_from_basket(self, user_id: int, data: ProductRequest):


        if "CPU" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.cpu_id == data.id
            )
        elif "GPU" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.gpu_id == data.id
            )
        elif "RAM" in data.article:
            query = query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.ram_id == data.id
            )
        elif "CASE" in data.article:
            query = query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.case_id == data.id
            )
        elif "M2" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.m2_id == data.id
            )
        elif "SSD" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.ssd_id == data.id
            )
        elif "HDD" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.hdd_id == data.id
            ).returning(Basket_Table)
        elif "MB" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.motherboard_id == data.id
            )
        elif "VENT" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.vent_id == data.id
            )
        elif "TOWER" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.cooler_id == data.id
            )
        elif "PU" in data.article:
            query = delete(Basket_Table).filter(
                Basket_Table.user_id == user_id,
                Basket_Table.pu_id == data.id
            )
        
        self.session.execute(query)
        self.session.commit()
    
    