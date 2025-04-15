from pydantic import BaseModel
from typing import Optional

class UserRegistration(BaseModel):
    login: str
    password: str
    email: str
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]


