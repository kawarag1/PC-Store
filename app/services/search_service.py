from app.database.connector import *
from app.models.models import *

from sqlalchemy import select
from fastapi import HTTPException
from collections import defaultdict


class SearchService():
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_products(self) -> dict[str, list]:
        grouped = defaultdict(list)

        models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]

        for model in models:
            query = select(model)
            
            products = (await self.session.execute(query)).scalars().all()
            grouped[model.__name__].extend(products)
        
        return dict(grouped)
        
    async def get_products_with_word(self, word: str) -> dict[str, list]:
        grouped = defaultdict(list)
        models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]

        for model in models:
            query = select(model).where(model.name.ilike(f"%{word}%"))
            products = (await self.session.execute(query)).scalars().all()
            if products:
                grouped[model.__name__].extend(products)
        
        
        return dict(grouped)
                
    async def get_filter_products(self, filter:str) -> dict[str, list]:
        filter_to_models = {
            "Процессор": CPU,
            "Видеокарт": GPU,
            "Оперативная память": RAM,
            "Кулер": Cooler,
            "Блок питания": POWER_UNIT,
            "Корпус": PC_CASE,
            "Жёсткий диск": HDD,
            "Твердотельный накопитель": SSD,
            "M2 накопитель": M2_SSD,
            "Материнская плата": Motherboard,
            "Вентилятор": VENT
        }

        try:
            model = filter_to_models[filter]
            query = select(model)
            result = await self.session.execute(query)
            return result.scalars().all()

        except:
            raise HTTPException(status_code = 404, detail = "filter not found")
        
        