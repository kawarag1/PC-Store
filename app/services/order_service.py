from app.models.models import Basket, Order, User
from app.database.connector import *

from fastapi import Depends, HTTPException
from sqlalchemy import select

from app.services.basket_service import BasketService
from app.schemas.request.order_schema import Order as OrderClass
from app.schemas.request.product import Product as ProductRequest
from app.security.jwtmanager import get_current_user

class OrderService():
    def __init__(self, session: Session):
        self.session = session


    async def check_orders(self, user_id: int):
        query = select(Order).filter(Order.user_id == user_id)

        result = self.session.execute(query)
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
                category_id = 1
            ).returning(Order)
        elif "GPU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "RAM" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "CASE" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "M2" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "SSD" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "HDD" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "MB" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "VENT" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "TOWER" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        elif "PU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1
            ).returning(Order)
        
        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()
    


    async def create_order(self, order: ProductRequest, user_id: int):
        query = insert(Order).values(
            user_id = user_id,
            category_id = 1,
            products_id = order.products_id,
            cpu_id = order.cpu_id,
            gpu_id = order.gpu_id,
            ram_id = order.ram_id,
            motherboard_id = order.motherboard_id,
            m2_id = order.m2_id,
            ssd_id = order.ssd_id,
            hdd_id = order.hdd_id,
            case_id = order.case_id,
            cooler_id = order.cooler_id,
            pu_id = order.pu_id
        ).returning(Order)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()
