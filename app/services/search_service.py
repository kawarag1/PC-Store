from app.database.connector import *
from app.models.models import *

from sqlalchemy import select
from fastapi import HTTPException
from collections import defaultdict


class SearchService():
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_products(self, word: str | None = None) -> dict[str, list]:
        grouped = defaultdict(list)

        models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]

        for model in models:
            if word:
                query = select(model).where(model.name.ilike(f"{word}%"))
                # query.where(model.name.ilike(f"%{word}%"))
            else:
                query = select(model)
            
            products = (await self.session.execute(query)).scalars().all()
            grouped[model.__name__].extend(products)
        
        return dict(grouped)

    async def get_filter_products(self, filter:str) -> dict[str, list]:
        try:
            if filter == "Процессоры":
                query = select(CPU)
            elif filter == "Видеокарты":
                query = select(GPU)
            elif filter == "Оперативная память":
                query = select(RAM)
            elif filter == "Кулер":
                query = select(Cooler)
            elif filter == "Блок питания":
                query = select(POWER_UNIT)
            elif filter == "Корпус":
                query = select(PC_CASE)
            elif filter == "Жёсткий диск":
                query = select(HDD)
            elif filter == "Твердотельный накопитель":
                query = select(SSD)
            elif filter == "M2 накопитель":
                query = select(M2_SSD)
            elif filter == "Материнская плата":
                query = select(Motherboard)
            elif filter == "Вентиляторы":
                query = select(VENT)

            result = await self.session.execute(query)
            return result.scalars().all()

        except:
            raise HTTPException(status_code = 404, detail = "filter not found")
        
        