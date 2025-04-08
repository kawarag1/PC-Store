from app.models.models import *

from enum import Enum

class Filters(Enum):
    CPU = "Процесс"
    GPU = "Видеокарта"
    RAM = "Оперативная память"
    Cooler = "Кулер"
    POWER_UNIT = "Блок питания"
    PC_CASE = "Корпус"
    HDD = "Жёсткий диск"
    SSD = "Твердотельный накопитель"
    M2_SSD = "М2 накопитель" # М - русская
    Motherboard = "Материнская плата"
    VENT = "Вентилятор"
    
    @classmethod
    def get_method(cls, filter):
        mapping = {
            cls.CPU: CPU,
            cls.GPU: GPU,
            cls.RAM: RAM,
            cls.Cooler: Cooler,
            cls.POWER_UNIT: POWER_UNIT,
            cls.PC_CASE: PC_CASE,
            cls.HDD: HDD,
            cls.SSD: SSD,
            cls.M2_SSD: M2_SSD,
            cls.Motherboard: Motherboard,
            cls.VENT: VENT
        }
        return mapping.get(filter)

