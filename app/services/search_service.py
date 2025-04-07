from app.database.connector import *
from app.models.models import *

from sqlalchemy import select
from collections import defaultdict


class SearchService():
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_products(self, word: str | None = None) -> dict[str, list]:
        grouped = defaultdict(list)

        models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]

        for model in models:
            query = select(model)
            if word:
                query.where(model.name.ilike(f"%{word}%"))
            
            products = (await self.session.execute(query)).scalars().all()
            grouped[model.__name__].extend(products)
        
        return dict(grouped)