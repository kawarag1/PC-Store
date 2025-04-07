from pydantic import BaseModel
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

from app.models.models import *


CPUModel = sqlalchemy_to_pydantic(CPU)
GPUModel = sqlalchemy_to_pydantic(GPU)
RAMModel = sqlalchemy_to_pydantic(RAM)
MBModel = sqlalchemy_to_pydantic(Motherboard)
PUModel = sqlalchemy_to_pydantic(POWER_UNIT)
CaseModel = sqlalchemy_to_pydantic(PC_CASE)
HDDModel = sqlalchemy_to_pydantic(HDD)
SSDModel = sqlalchemy_to_pydantic(SSD)
M2Model = sqlalchemy_to_pydantic(M2_SSD)
VentModel = sqlalchemy_to_pydantic(VENT)
CoolerModel = sqlalchemy_to_pydantic(Cooler)

class Products(BaseModel):
    CPU: CPUModel
    GPU: GPUModel
    RAM: RAMModel
    Motherboard: MBModel
    PowerUnit: PUModel
    Case: CaseModel
    HDD: HDDModel
    SSD: SSDModel
    M2SSD: M2Model
    Vent: VentModel
    Cooler: CoolerModel


