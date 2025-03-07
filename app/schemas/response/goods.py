from pydantic import BaseModel
from typing import Optional



class Goods(BaseModel):
    products_id:Optional[int]
    cpu_id:Optional[int]
    gpu_id:Optional[int]
    ram_id:Optional[int]
    motherboard_id:Optional[int]
    m2_id:Optional[int]
    ssd_id:Optional[int]
    hdd_id:Optional[int]
    case_id:Optional[int]
    cooler_id:Optional[int]
    pu_id:Optional[int]
    