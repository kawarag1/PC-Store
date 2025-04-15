from pydantic import BaseModel


class Product(BaseModel):
    id:int
    article:str
