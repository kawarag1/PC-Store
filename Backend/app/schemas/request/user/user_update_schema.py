from pydantic import BaseModel
from typing import Optional

class UserUpdate(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None


