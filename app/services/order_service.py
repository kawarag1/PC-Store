from app.models.models import Order
from app.database.connector import *

from fastapi import HTTPException
from sqlalchemy import select

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