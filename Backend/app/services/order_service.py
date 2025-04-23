from app.models.models import Basket, Order, User
from app.database.connector import *

from fastapi import Depends, HTTPException
from sqlalchemy import select

from app.services.basket_service import BasketService
from app.schemas.request.order_schema import Order as OrderClass
from app.schemas.request.product import Product as ProductRequest
from app.security.jwtmanager import get_current_user

class OrderService():
    def __init__(self, session: AsyncSession):
        self.session = session


    async def check_orders(self, user_id: int):
        query = select(Order).filter(Order.user_id == user_id)

        result = await self.session.execute(query)
        orders = result.scalars().all()
        if orders is None:
            raise HTTPException(
                status_code = 404,
                detail = "На данный момент у вас нет заказов"
            )
        return orders
    

    async def create_fast_order(self, order: ProductRequest, user_id: int):
        if "CPU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "GPU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                gpu_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "RAM" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                ram_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "CASE" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                case_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "M2" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                m2_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "SSD" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                ssd_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "HDD" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                hdd_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "MB" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                motherboard_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "VENT" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                vent_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "TOWER" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cooler_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "PU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                pu_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        

        await BasketService(self.session).delete_one_from_basket(user_id, order)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalars().first()
    


    async def create_order(self, user_id: int, cost: int):

        baskets = await BasketService(self.session).check_basket(user_id)

        for item in range(len(baskets)):
            basket = baskets[item]

            query = insert(Order).values(
            user_id = user_id,
            category_id = 1,
            sum = cost,
            products_id = basket.products_id,
            cpu_id = basket.cpu_id,
            gpu_id = basket.gpu_id,
            ram_id = basket.ram_id,
            motherboard_id = basket.motherboard_id,
            m2_id = basket.m2_id,
            ssd_id = basket.ssd_id, 
            hdd_id = basket.hdd_id,
            case_id = basket.case_id,
            cooler_id = basket.cooler_id,
            pu_id = basket.pu_id
        ).returning(Order)
            
            result = await self.session.execute(query)
            await self.session.commit()

        await BasketService(self.session).basket_clear(user_id)
        return result.scalars().first()

        #надо будет оптимизировать, так как будет генерироваться не 1 общий заказ