from enum import Enum
import random
class ItemsTypes(Enum):
    GPU = "GPU-"
    CPU = "CPU-"
    RAM = "RAM-"
    CASE = "CASE-"
    M2 = "M2-"
    SSD = "SSD-"
    HDD = "HDD-"
    MB = "MB-" #motherboard
    VENT = "VENT-"
    TOWER = "TOWER-"
    PU = "PU-" #power unit
    PC = "PC-"
    


def generate_articul(type: ItemsTypes) -> str:
    return f"{type.value}{random.randint(100_000_000, 999_999_999)}"
