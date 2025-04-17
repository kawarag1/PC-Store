from app.database.connector import *
from app.models.models import *
from app.schemas.request.filters import Filters

from sqlalchemy import select, join
from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from collections import defaultdict


class SearchService():
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_products(self) -> dict[str, list]:
        grouped = defaultdict(list)

        models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]
        filter_for_search = {
            CPU: [
                selectinload(CPU.manufacturers)
            ],
            GPU: [
                selectinload(GPU.manufacturers)
            ],
            RAM: [
                selectinload(RAM.manufacturers)
            ],
            Motherboard: [
                selectinload(Motherboard.manufacturers)
            ],
            POWER_UNIT: [
                selectinload(POWER_UNIT.manufacturers),
                selectinload(POWER_UNIT.certs)
            ],
            PC_CASE: [
                selectinload(PC_CASE.manufacturers)
            ],
            HDD: [
                selectinload(HDD.manufacturers)
            ],
            SSD: [
                selectinload(SSD.manufacturers)
            ],
            M2_SSD: [
                selectinload(M2_SSD.manufacturers),
                selectinload(M2_SSD.m2Size)
            ],
            VENT: [
                selectinload(VENT.manufacturers)
            ],
            Cooler: [
                selectinload(Cooler.manufacturers)
            ]
        }

        for model in models:
            if model in filter_for_search:
                for option in filter_for_search[model]:

                    query = select(model).options(option)
            
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
        try:
            product_type = Filters(filter)
            model = Filters.get_model(product_type)
            query = select(model).join()
            result = await self.session.execute(query)
            return result.scalars().all()

        except:
            raise HTTPException(status_code = 404, detail = "filter not found")
        
        