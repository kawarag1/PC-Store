from pydantic import BaseModel
from typing import Optional

class UserUpdate(BaseModel):
    login: Optional[str]
    password: Optional[str]
    email: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]


