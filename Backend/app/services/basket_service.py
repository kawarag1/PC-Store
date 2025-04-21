from app.models.models import *
from app.schemas.request import basket_schema
from app.schemas.request.basket_schema import Basket as Basket_Schema
from app.schemas.request.product import Product as ProductRequest
from app.database.connector import *
from app.schemas.response.goods import Goods


from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload, defer
from typing import List



class BasketService():
    query_options = [
        selectinload(Basket.cpus).defer(CPU.cpu_specs_id),
        selectinload(Basket.cpus).defer(CPU.manufacturer_id),
        selectinload(Basket.cpus).selectinload(CPU.specs).selectinload(CPU_SPECS.sockets),
        selectinload(Basket.cpus).selectinload(CPU.manufacturers),

        selectinload(Basket.gpus).defer(GPU.gpu_specs_id),
        selectinload(Basket.gpus).defer(GPU.manufacturer_id),
        selectinload(Basket.gpus).selectinload(GPU.specs).defer(GPU_SPECS.video_memory_type).selectinload(GPU_SPECS.GPU_Memory_Types),
        selectinload(Basket.gpus).selectinload(GPU.manufacturers),

        selectinload(Basket.rams).defer(RAM.ram_specs_id),
        selectinload(Basket.rams).defer(RAM.manufacturer_id),
        selectinload(Basket.rams).selectinload(RAM.specs).defer(RAM_SPECS.type_id).selectinload(RAM_SPECS.types),
        selectinload(Basket.rams).selectinload(RAM.specs).defer(RAM_SPECS.ram_quantity).selectinload(RAM_SPECS.ram_quantities),
        selectinload(Basket.rams).selectinload(RAM.manufacturers),

        selectinload(Basket.motherboards).defer(Motherboard.motherboard_specs_id),
        selectinload(Basket.motherboards).defer(Motherboard.manufacturer_id),
        selectinload(Basket.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.form).selectinload(Motherboard_SPECS.forms),
        selectinload(Basket.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.chipset).selectinload(Motherboard_SPECS.chipsets),
        selectinload(Basket.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.socket).selectinload(Motherboard_SPECS.sockets),
        selectinload(Basket.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.M2_Slot).selectinload(Motherboard_SPECS.slots),
        selectinload(Basket.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.RAM_Type_id).selectinload(Motherboard_SPECS.ram_types),
        selectinload(Basket.motherboards).selectinload(Motherboard.manufacturers),


        selectinload(Basket.puS).defer(POWER_UNIT.manufacturer_id),
        selectinload(Basket.puS).defer(POWER_UNIT.certificate_id),
        selectinload(Basket.puS).selectinload(POWER_UNIT.manufacturers),
        selectinload(Basket.puS).selectinload(POWER_UNIT.certs),


        selectinload(Basket.cases).defer(PC_CASE.pc_case_specs_id),
        selectinload(Basket.cases).defer(PC_CASE.manufacturer_id),
        selectinload(Basket.cases).selectinload(PC_CASE.specs).defer(PC_CASE_SPECS.vent_size).selectinload(PC_CASE_SPECS.sizes),
        selectinload(Basket.cases).selectinload(PC_CASE.specs).defer(PC_CASE_SPECS.case_type).selectinload(PC_CASE_SPECS.types),
        selectinload(Basket.cases).selectinload(PC_CASE.manufacturers),


        selectinload(Basket.hddS).defer(HDD.hdd_specs_id),
        selectinload(Basket.hddS).defer(HDD.manufacturer_id),
        selectinload(Basket.hddS).selectinload(HDD.specs).defer(HDD_SPECS.memory_id).selectinload(HDD_SPECS.memories),
        selectinload(Basket.hddS).selectinload(HDD.manufacturers),


        selectinload(Basket.ssdS).defer(SSD.ssd_specs_id),
        selectinload(Basket.ssdS).defer(SSD.manufacturer_id),
        selectinload(Basket.ssdS).selectinload(SSD.specs).defer(SSD_SPECS.memory_id).selectinload(SSD_SPECS.memories),
        selectinload(Basket.ssdS).selectinload(SSD.manufacturers),


        selectinload(Basket.m2_ssdS).defer(M2_SSD.m2_ssd_specs_id),
        selectinload(Basket.m2_ssdS).defer(M2_SSD.manufacturer_id),
        selectinload(Basket.m2_ssdS).defer(M2_SSD.size),
        selectinload(Basket.m2_ssdS).selectinload(M2_SSD.specs).defer(M2_SSD_SPECS.memory_id).selectinload(M2_SSD_SPECS.memories),
        selectinload(Basket.m2_ssdS).selectinload(M2_SSD.manufacturers),
        selectinload(Basket.m2_ssdS).selectinload(M2_SSD.m2Size),


        selectinload(Basket.vents).defer(VENT.specs_id),
        selectinload(Basket.vents).defer(VENT.manufacturer_id),
        selectinload(Basket.vents).selectinload(VENT.specs),
        selectinload(Basket.vents).selectinload(VENT.manufacturers),


        selectinload(Basket.coolers).defer(Cooler.cooler_specs_id),
        selectinload(Basket.coolers).defer(Cooler.manufacturer_id),
        selectinload(Basket.coolers).selectinload(Cooler.specs).defer(Cooler_Specs.base_material_id).selectinload(Cooler_Specs.base_material),
        selectinload(Basket.coolers).selectinload(Cooler.specs).defer(Cooler_Specs.radiator_material_id).selectinload(Cooler_Specs.radiator_material),
        selectinload(Basket.coolers).selectinload(Cooler.coolers_sockets).selectinload(Cooler_Socket.sockets),
        selectinload(Basket.coolers).selectinload(Cooler.manufacturers)
    ]
    def __init__(self, session:AsyncSession):
        self.session = session

    async def check_basket(self, user_id : int) -> List[Basket_Schema]:
        query = select(Basket).filter(Basket.user_id == user_id).options(*self.query_options)

        products = (await self.session.execute(query)).scalars().all()
        if products:
            for product in products:
                product.image = f"http://localhost:13280/{product.image}.jpg"

        if products is None:
            raise HTTPException(
                status_code = 404,
                detail = "Ваша корзина пуста"
            )
        return products
        
    

    async def add_to_basket(self, data: ProductRequest, user_id: int):
        if "CPU" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                cpu_id = data.id
            ).returning(Basket)
        elif "GPU" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                gpu_id = data.id
            ).returning(Basket)
        elif "RAM" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                ram_id = data.id
            ).returning(Basket)
        elif "CASE" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                case_id = data.id
            ).returning(Basket)
        elif "M2" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                m2_id = data.id
            ).returning(Basket)
        elif "SSD" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                ssd_id = data.id
            ).returning(Basket)
        elif "HDD" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                hdd_id = data.id
            ).returning(Basket)
        elif "MB" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                motherboard_id = data.id
            ).returning(Basket)
        elif "VENT" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                vent_id = data.id
            ).returning(Basket)
        elif "TOWER" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                cooler_id = data.id
            ).returning(Basket)
        elif "PU" in data.article:
            query = insert(Basket).values(
                user_id = user_id,
                pu_id = data.id
            ).returning(Basket)
        
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalars().first()



    async def basket_clear(self, user_id: int):
        query = delete(Basket).filter(Basket.user_id == user_id)

        await self.session.execute(query)
        await self.session.commit()
        


    async def delete_one_from_basket(self, user_id: int, data: ProductRequest):
        if "CPU" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.cpu_id == data.id
            )
        elif "GPU" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.gpu_id == data.id
            )
        elif "RAM" in data.article:
            query = query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.ram_id == data.id
            )
        elif "CASE" in data.article:
            query = query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.case_id == data.id
            )
        elif "M2" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.m2_id == data.id
            )
        elif "SSD" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.ssd_id == data.id
            )
        elif "HDD" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.hdd_id == data.id
            ).returning(Basket)
        elif "MB" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.motherboard_id == data.id
            )
        elif "VENT" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.vent_id == data.id
            )
        elif "TOWER" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.cooler_id == data.id
            )
        elif "PU" in data.article:
            query = delete(Basket).filter(
                Basket.user_id == user_id,
                Basket.pu_id == data.id
            )
        
        await self.session.execute(query)
        await self.session.commit()
    
    