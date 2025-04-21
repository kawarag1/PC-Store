from pydantic import BaseModel
from typing import Optional



class Basket(BaseModel):
    products_id:Optional[int] = None
    cpu_id:Optional[int] = None
    gpu_id:Optional[int] = None
    ram_id:Optional[int] = None
    motherboard_id:Optional[int] = None
    m2_id:Optional[int] = None
    ssd_id:Optional[int] = None
    hdd_id:Optional[int] = None
    case_id:Optional[int] = None
    cooler_id:Optional[int] = None
    pu_id:Optional[int] = None
    vent_id:Optional[int] = None
    