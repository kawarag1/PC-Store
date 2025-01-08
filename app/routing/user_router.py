from app.database.connector import get_session
from app.schemas.requests.user_schema import UserRequest

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.services.user_service import UserService


router = APIRouter(
    prefix="/user"
)

@router.post("/registration")
async def reg(data: UserRequest, session: Session = Depends(get_session)):
    return UserService.registration(data)