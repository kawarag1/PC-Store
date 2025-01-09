from app.database.connector import get_session
from app.schemas.requests.user_schema import UserRequest, UserAuth

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.services.user_register import UserRegister
from app.services.user_profile import UserProfile
from app.services.user_authtorization import UserAuthtorization


router = APIRouter(
    prefix="/user"
)

@router.post("/registration")
async def reg(request: UserRequest, session: Session = Depends(get_session)):
    result = await UserRegister(session).register(request)
    return result


@router.get("/profile/{login}")
async def profile(login:str, session: Session = Depends(get_session)):
    result = await UserProfile(session).get_profile(login)
    return result

@router.post("/authtorization")
async def authtorization(request: UserAuth, session:Session = Depends(get_session)):
    result = await UserAuthtorization(session).authtorization(request.login, request.password)
    return result


