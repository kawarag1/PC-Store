from app.database.connector import *
from app.models.models import *
from app.schemas.request.filters import Filters

from sqlalchemy import select, join
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import defer
from fastapi import HTTPException
from collections import defaultdict


class SearchService():
    models = [CPU, GPU, RAM, Motherboard, POWER_UNIT, PC_CASE, HDD, SSD, M2_SSD, VENT, Cooler]
    filter_for_search = {
        CPU: [
            defer(CPU.cpu_specs_id),
            defer(CPU.manufacturer_id),
            selectinload(CPU.specs).selectinload(CPU_SPECS.sockets),
            selectinload(CPU.manufacturers)          
            ],
        GPU: [
            defer(GPU.gpu_specs_id),
            defer(GPU.manufacturer_id),
            selectinload(GPU.specs).defer(GPU_SPECS.video_memory_type).selectinload(GPU_SPECS.GPU_Memory_Types),
            selectinload(GPU.manufacturers)
            ],
        RAM: [
            defer(RAM.ram_specs_id),
            defer(RAM.manufacturer_id),
            selectinload(RAM.specs).defer(RAM_SPECS.type_id).selectinload(RAM_SPECS.types),
            selectinload(RAM.specs).defer(RAM_SPECS.ram_quantity).selectinload(RAM_SPECS.ram_quantities),
            selectinload(RAM.manufacturers)
            ],
        Motherboard: [
            defer(Motherboard.motherboard_specs_id),
            defer(Motherboard.manufacturer_id),
            selectinload(Motherboard.specs).defer(Motherboard_SPECS.form).selectinload(Motherboard_SPECS.forms),
            selectinload(Motherboard.specs).defer(Motherboard_SPECS.chipset).selectinload(Motherboard_SPECS.chipsets),
            selectinload(Motherboard.specs).defer(Motherboard_SPECS.socket).selectinload(Motherboard_SPECS.sockets),
            selectinload(Motherboard.specs).defer(Motherboard_SPECS.M2_Slot).selectinload(Motherboard_SPECS.slots),
            selectinload(Motherboard.specs).defer(Motherboard_SPECS.RAM_Type_id).selectinload(Motherboard_SPECS.ram_types),
            selectinload(Motherboard.manufacturers)
            ],
        POWER_UNIT: [
            defer(POWER_UNIT.manufacturer_id),
            defer(POWER_UNIT.certificate_id),
            selectinload(POWER_UNIT.manufacturers),
            selectinload(POWER_UNIT.certs)
            ],
        PC_CASE: [
            defer(PC_CASE.pc_case_specs_id),
            defer(PC_CASE.manufacturer_id),
            selectinload(PC_CASE.specs).defer(PC_CASE_SPECS.vent_size).selectinload(PC_CASE_SPECS.sizes),
            selectinload(PC_CASE.specs).defer(PC_CASE_SPECS.case_type).selectinload(PC_CASE_SPECS.types),
            selectinload(PC_CASE.manufacturers)
            ],
        HDD: [
            defer(HDD.hdd_specs_id),
            defer(HDD.manufacturer_id),
            selectinload(HDD.specs).defer(HDD_SPECS.memory_id).selectinload(HDD_SPECS.memories),
            selectinload(HDD.manufacturers)
            ],
        SSD: [
            defer(SSD.ssd_specs_id),
            defer(SSD.manufacturer_id),
            selectinload(SSD.specs).defer(SSD_SPECS.memory_id).selectinload(SSD_SPECS.memories),
            selectinload(SSD.manufacturers)
            ],
        M2_SSD: [
            defer(M2_SSD.m2_ssd_specs_id),
            defer(M2_SSD.manufacturer_id),
            defer(M2_SSD.size),
            selectinload(M2_SSD.specs).defer(M2_SSD_SPECS.memory_id).selectinload(M2_SSD_SPECS.memories),
            selectinload(M2_SSD.manufacturers),
            selectinload(M2_SSD.m2Size)
            ],
        VENT: [
            defer(VENT.specs_id),
            defer(VENT.manufacturer_id),
            selectinload(VENT.specs),
            selectinload(VENT.manufacturers)
            ],
        Cooler: [
            defer(Cooler.cooler_specs_id),
            defer(Cooler.manufacturer_id),
            selectinload(Cooler.specs).defer(Cooler_Specs.base_material_id).selectinload(Cooler_Specs.base_material),
            selectinload(Cooler.specs).defer(Cooler_Specs.radiator_material_id).selectinload(Cooler_Specs.radiator_material),
            selectinload(Cooler.coolers_sockets).selectinload(Cooler_Socket.sockets),
            selectinload(Cooler.manufacturers)
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
        try:
            grouped = defaultdict(list)

            for model in self.models:
                query = select(model).where(model.name.ilike(f"%{word}%"))
                if model in self.filter_for_search:
                    query = query.options(*self.filter_for_search[model])
                products = (await self.session.execute(query)).scalars().all()
                if products:
                    for product in products:
                        product.image = f"http://localhost:13280{product.image}"
                        grouped[model.__name__].extend(products)

        
            return dict(grouped)
        except:
            raise HTTPException(status_code  = 404, detail = "product not found")
                
    async def get_filter_products(self, filter:str) -> dict[str, list]:
        try:
            product_type = Filters(filter)
            model = Filters.get_model(product_type)
            query = select(model)
            if model in self.filter_for_search:
                for option in self.filter_for_search[model]:
                    query = query.options(option)
            result = await self.session.execute(query)
            return result.scalars().all()

        except:
            raise HTTPException(status_code = 404, detail = "filter not found")
        
        