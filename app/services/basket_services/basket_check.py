from app.models.models import Basket
from app.schemas.requests import basket_schema
from app.database.connector import *

from fastapi import HTTPException
from sqlalchemy import select


class BasketCheck():
    def __init__(self, session:Session):
        self.session = session

    async def check(self, user_id:int):
        query = select(Basket).filter(Basket.user_id == user_id)

        result = self.session.execute(query)
        return result.scalar