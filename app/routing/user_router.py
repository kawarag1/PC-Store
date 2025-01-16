from app.database.connector import get_session
from app.schemas.request.user.user_registration_schema import UserRegistration
from app.schemas.request.user.user_auth_schema import UserAuth
from app.schemas.request.user.user_update_schema import UserUpdate

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.services.user_service import UserService 


router = APIRouter(
    prefix="/user"
)

@router.post("/registration")
async def reg(request: UserRegistration, session: Session = Depends(get_session)):
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


@router.put("/update_profile")
async def update_profile(request: UserUpdate, user_id: int, session: Session = Depends(get_session)):
    result = await UserService(session).update_profile(user_id, request)
    return result
