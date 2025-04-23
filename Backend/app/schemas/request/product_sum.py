from pydantic import BaseModel
from typing import Optional

class ProductSum(BaseModel):
    sum: Optional[int]