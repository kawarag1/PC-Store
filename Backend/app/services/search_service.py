from app.database.connector import *
from app.models.models import *
from app.schemas.request.filters import Filters

from sqlalchemy import select, join
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import joinedload
from fastapi import HTTPException
from collections import defaultdict


class SearchService():
    models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]
    filter_for_search = {
        CPU: [
            selectinload(CPU.specs).selectinload(CPU_SPECS.sockets),
            selectinload(CPU.manufacturers)            
            ],
        GPU: [
            selectinload(GPU.specs).selectinload(GPU_SPECS.GPU_Memory_Types),
            selectinload(GPU.manufacturers)
            ],
        RAM: [
            selectinload(RAM.specs).selectinload(RAM_SPECS.types),
            selectinload(RAM.specs).selectinload(RAM_SPECS.ram_quantities),
            selectinload(RAM.manufacturers)
            ],
        Motherboard: [
            selectinload(Motherboard.specs).selectinload(Motherboard_SPECS.forms),
            selectinload(Motherboard.specs).selectinload(Motherboard_SPECS.chipsets),
            selectinload(Motherboard.specs).selectinload(Motherboard_SPECS.sockets),
            selectinload(Motherboard.specs).selectinload(Motherboard_SPECS.slots),
            selectinload(Motherboard.specs).selectinload(Motherboard_SPECS.ram_types),
            selectinload(Motherboard.manufacturers)
            ],
        POWER_UNIT: [
            selectinload(POWER_UNIT.manufacturers),
            selectinload(POWER_UNIT.certs)
            ],
        PC_CASE: [
            selectinload(PC_CASE.specs).selectinload(PC_CASE_SPECS.sizes),
            selectinload(PC_CASE.specs).selectinload(PC_CASE_SPECS.types),
            selectinload(PC_CASE.manufacturers)
            ],
        HDD: [
            selectinload(HDD.specs).selectinload(HDD_SPECS.memories),
            selectinload(HDD.manufacturers)
            ],
        SSD: [
            selectinload(SSD.specs).selectinload(SSD_SPECS.memories),
            selectinload(SSD.manufacturers)
            ],
        M2_SSD: [
            selectinload(M2_SSD.specs).selectinload(M2_SSD_SPECS.memories),
            selectinload(M2_SSD.manufacturers),
            selectinload(M2_SSD.m2Size)
            ],
        VENT: [
            selectinload(VENT.specs),
            selectinload(VENT.manufacturers)
            ],
        Cooler: [
            selectinload(Cooler.specs).selectinload(Cooler_Specs.base_material),
            selectinload(Cooler.specs).selectinload(Cooler_Specs.radiator_material),
            selectinload(Cooler.coolers_sockets).selectinload(Cooler_Socket.sockets),
            selectinload(Cooler.manufacturers),
            ]
        }

    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_all_products(self) -> dict[str, list]:
        grouped = defaultdict(list)

        
        

        for model in self.models:
            query = select(model)
            if model in self.filter_for_search:
                for option in self.filter_for_search[model]:

                    query = query.options(option)
            
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
        
        