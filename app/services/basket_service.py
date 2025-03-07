from app.models.models import Basket as Basket_Table, User
from app.schemas.request import basket_schema
from app.schemas.request.basket_schema import Basket
from app.database.connector import *
from app.schemas.response.goods import Goods


from fastapi import Depends, HTTPException
from sqlalchemy import select

from app.security.jwtmanager import get_current_user


class BasketService():
    def __init__(self, session:Session):
        self.session = session

    async def check_basket(self, user_id : int) -> list[Goods]:
        query = select(Basket_Table).filter(Basket_Table.user_id == user_id)

        result = self.session.execute(query)
        basket = result.scalars().all()
        if basket is None:
            raise HTTPException(
                status_code = 404,
                detail = "Ваша корзина пуста"
            )
        goods_list = []
        for item in basket:
            goods_list.append(Goods(
                products_id = item.products_id,
                cpu_id = item.cpu_id,
                gpu_id = item.gpu_id,
                ram_id = item.ram_id,
                motherboard_id = item.motherboard_id,
                m2_id = item.m2_id,
                ssd_id = item.ssd_id,
                hdd_id = item.hdd_id,
                case_id = item.case_id,
                cooler_id = item.cooler_id,
                pu_id = item.pu_id
            ))
        return goods_list
        
    

    async def add_to_basket(self, data: Basket, user_id: int):
        if not isinstance(data, Basket):
             raise ValueError("data должен быть экземпляром Basket")
        
        query = insert(Basket_Table).values(
            user_id = user_id,
            products_id = data.products_id,
            cpu_id = data.cpu_id,
            gpu_id = data.gpu_id,
            ram_id = data.ram_id,
            motherboard_id = data.motherboard_id,
            m2_id = data.m2_id,
            ssd_id = data.ssd_id,
            hdd_id = data.hdd_id,
            case_id = data.case_id,
            cooler_id = data.cooler_id,
            pu_id = data.pu_id
        ).returning(Basket_Table)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()
        
    