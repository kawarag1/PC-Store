from app.database.connector import get_session
from app.schemas.requests.user_schema import UserRequest

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.services.user_service import UserService
from app.services.user_profile import UserProfile


router = APIRouter(
    prefix="/user"
)

@router.post("/registration")
async def reg(request: UserRequest, session: Session = Depends(get_session)):
    result = await UserService(session).register(request)
    return result


@router.get("/profile/{login}")
async def profile(login:str, session: Session = Depends(get_session)):
    result = await UserProfile(session).get_profile(login)
    return result