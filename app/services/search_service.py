from app.schemas.request.products import Products
from app.database.connector import *
from app.models.models import *

from sqlalchemy import select


class SearchService():
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_products(self, word: str | None = None) -> list[Products]:
        all_products = []

        models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]

        for model in models:
            query = select(model)
            if word:
                query.where(model.name.ilike(f"%{word}%"))
            
        
            result = await self.session.execute(query)
            products = result.scalars().all()
            all_products.extend(products)
        
        return all_products