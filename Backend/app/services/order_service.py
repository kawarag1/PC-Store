from app.models.models import Basket, Order, User
from app.database.connector import *

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload, defer

from app.services.basket_service import BasketService
from app.schemas.request.order_schema import Order as OrderClass
from app.schemas.request.product import Product as ProductRequest
from app.security.jwtmanager import get_current_user

class OrderService():
    query_options = [
        defer(Order.cpu_id),
        defer(Order.gpu_id),
        defer(Order.products_id),
        defer(Order.ram_id),
        defer(Order.motherboard_id),
        defer(Order.m2_id),
        defer(Order.ssd_id),
        defer(Order.hdd_id),
        defer(Order.case_id),
        defer(Order.cooler_id),
        defer(Order.pu_id),
        defer(Order.vent_id),
        selectinload(Order.cpus).defer(CPU.cpu_specs_id),
        selectinload(Order.cpus).defer(CPU.manufacturer_id),
        selectinload(Order.cpus).selectinload(CPU.specs).selectinload(CPU_SPECS.sockets),
        selectinload(Order.cpus).selectinload(CPU.manufacturers),

        selectinload(Order.gpus).defer(GPU.gpu_specs_id),
        selectinload(Order.gpus).defer(GPU.manufacturer_id),
        selectinload(Order.gpus).selectinload(GPU.specs).defer(GPU_SPECS.video_memory_type).selectinload(GPU_SPECS.GPU_Memory_Types),
        selectinload(Order.gpus).selectinload(GPU.manufacturers),

        selectinload(Order.rams).defer(RAM.ram_specs_id),
        selectinload(Order.rams).defer(RAM.manufacturer_id),
        selectinload(Order.rams).selectinload(RAM.specs).defer(RAM_SPECS.type_id).selectinload(RAM_SPECS.types),
        selectinload(Order.rams).selectinload(RAM.specs).defer(RAM_SPECS.ram_quantity).selectinload(RAM_SPECS.ram_quantities),
        selectinload(Order.rams).selectinload(RAM.manufacturers),

        selectinload(Order.motherboards).defer(Motherboard.motherboard_specs_id),
        selectinload(Order.motherboards).defer(Motherboard.manufacturer_id),
        selectinload(Order.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.form).selectinload(Motherboard_SPECS.forms),
        selectinload(Order.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.chipset).selectinload(Motherboard_SPECS.chipsets),
        selectinload(Order.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.socket).selectinload(Motherboard_SPECS.sockets),
        selectinload(Order.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.M2_Slot).selectinload(Motherboard_SPECS.slots),
        selectinload(Order.motherboards).selectinload(Motherboard.specs).defer(Motherboard_SPECS.RAM_Type_id).selectinload(Motherboard_SPECS.ram_types),
        selectinload(Order.motherboards).selectinload(Motherboard.manufacturers),


        selectinload(Order.puS).defer(POWER_UNIT.manufacturer_id),
        selectinload(Order.puS).defer(POWER_UNIT.certificate_id),
        selectinload(Order.puS).selectinload(POWER_UNIT.manufacturers),
        selectinload(Order.puS).selectinload(POWER_UNIT.certs),


        selectinload(Order.cases).defer(PC_CASE.pc_case_specs_id),
        selectinload(Order.cases).defer(PC_CASE.manufacturer_id),
        selectinload(Order.cases).selectinload(PC_CASE.specs).defer(PC_CASE_SPECS.vent_size).selectinload(PC_CASE_SPECS.sizes),
        selectinload(Order.cases).selectinload(PC_CASE.specs).defer(PC_CASE_SPECS.case_type).selectinload(PC_CASE_SPECS.types),
        selectinload(Order.cases).selectinload(PC_CASE.manufacturers),


        selectinload(Order.hddS).defer(HDD.hdd_specs_id),
        selectinload(Order.hddS).defer(HDD.manufacturer_id),
        selectinload(Order.hddS).selectinload(HDD.specs).defer(HDD_SPECS.memory_id).selectinload(HDD_SPECS.memories),
        selectinload(Order.hddS).selectinload(HDD.manufacturers),


        selectinload(Order.ssdS).defer(SSD.ssd_specs_id),
        selectinload(Order.ssdS).defer(SSD.manufacturer_id),
        selectinload(Order.ssdS).selectinload(SSD.specs).defer(SSD_SPECS.memory_id).selectinload(SSD_SPECS.memories),
        selectinload(Order.ssdS).selectinload(SSD.manufacturers),


        selectinload(Order.m2_ssdS).defer(M2_SSD.m2_ssd_specs_id),
        selectinload(Order.m2_ssdS).defer(M2_SSD.manufacturer_id),
        selectinload(Order.m2_ssdS).defer(M2_SSD.size),
        selectinload(Order.m2_ssdS).selectinload(M2_SSD.specs).defer(M2_SSD_SPECS.memory_id).selectinload(M2_SSD_SPECS.memories),
        selectinload(Order.m2_ssdS).selectinload(M2_SSD.manufacturers),
        selectinload(Order.m2_ssdS).selectinload(M2_SSD.m2Size),


        selectinload(Order.vents).defer(VENT.specs_id),
        selectinload(Order.vents).defer(VENT.manufacturer_id),
        selectinload(Order.vents).selectinload(VENT.specs),
        selectinload(Order.vents).selectinload(VENT.manufacturers),


        selectinload(Order.coolers).defer(Cooler.cooler_specs_id),
        selectinload(Order.coolers).defer(Cooler.manufacturer_id),
        selectinload(Order.coolers).selectinload(Cooler.specs).defer(Cooler_Specs.base_material_id).selectinload(Cooler_Specs.base_material),
        selectinload(Order.coolers).selectinload(Cooler.specs).defer(Cooler_Specs.radiator_material_id).selectinload(Cooler_Specs.radiator_material),
        selectinload(Order.coolers).selectinload(Cooler.coolers_sockets).selectinload(Cooler_Socket.sockets),
        selectinload(Order.coolers).selectinload(Cooler.manufacturers)
    ]
    def __init__(self, session: AsyncSession):
        self.session = session


    async def check_orders(self, user_id: int):
        query = select(Order).filter(Order.user_id == user_id).options(*self.query_options)

        result = await self.session.execute(query)
        orders = result.scalars().all()
        if orders is None:
            raise HTTPException(
                status_code = 404,
                detail = "На данный момент у вас нет заказов"
            )
        return orders
    

    async def create_fast_order(self, order: ProductRequest, user_id: int):
        if "CPU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cpu_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "GPU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                gpu_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "RAM" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                ram_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "CASE" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                case_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "M2" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                m2_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "SSD" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                ssd_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "HDD" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                hdd_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "MB" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                motherboard_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "VENT" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                vent_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "TOWER" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                cooler_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        elif "PU" in order.article:
            query = insert(Order).values(
                user_id = user_id,
                pu_id = order.id,
                category_id = 1,
                sum = order.cost
            ).returning(Order)
        

        await BasketService(self.session).delete_one_from_basket(user_id, order)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalars().first()
    


    async def create_order(self, user_id: int, cost: int):

        baskets = await BasketService(self.session).check_basket(user_id)

        for item in range(len(baskets)):
            basket = baskets[item]

            query = insert(Order).values(
            user_id = user_id,
            category_id = 1,
            sum = cost,
            products_id = basket.products_id,
            cpu_id = basket.cpu_id,
            gpu_id = basket.gpu_id,
            ram_id = basket.ram_id,
            motherboard_id = basket.motherboard_id,
            m2_id = basket.m2_id,
            ssd_id = basket.ssd_id, 
            hdd_id = basket.hdd_id,
            case_id = basket.case_id,
            cooler_id = basket.cooler_id,
            pu_id = basket.pu_id
        ).returning(Order)
            
            result = await self.session.execute(query)
            await self.session.commit()

        await BasketService(self.session).basket_clear(user_id)
        return result.scalars().first()

        #надо будет оптимизировать, так как будет генерироваться не 1 общий заказ