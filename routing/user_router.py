from fastapi import APIRouter, Depends
from database.config import *


from services import user_service as UserService
from schemas.requests import user_schema


router = APIRouter()

@router.post("/registration", tags = ["user"])
async def reg(data: user_schema.UserRequest = None):
    return UserService.registration(data)