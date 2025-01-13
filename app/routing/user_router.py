from app.database.connector import get_session
from app.schemas.request.user.user_registration_schema import UserRequest
from app.schemas.request.user.user_auth_schema import UserAuth

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.services.user_schema import UserService 


router = APIRouter(
    prefix="/user"
)

@router.post("/registration")
async def reg(request: UserRequest, session: Session = Depends(get_session)):
    result = await UserService(session).register(request)
    return result


@router.get("/profile/{login}")
async def profile(login: str, session: Session = Depends(get_session)):
    result = await UserService(session).get_profile(login)
    return result

@router.post("/authtorization")
async def authtorization(request: UserAuth, session: Session = Depends(get_session)):
    result = await UserService(session).authtorization(request.login, request.password)
    return result


