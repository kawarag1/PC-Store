from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int]
    article: Optional[str]
    cost: Optional[int] = 0
