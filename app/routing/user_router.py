from fastapi.responses import JSONResponse
from app.database.connector import get_session
from app.models.models import User
from app.schemas.request.user.user_registration_schema import UserRegistration
from app.schemas.request.user.user_auth_schema import UserAuth
from app.schemas.request.user.user_update_schema import UserUpdate


from fastapi import APIRouter, Depends, Form, HTTPException, Request

from sqlalchemy.orm import Session


from app.schemas.response.access_token import AccessToken
from app.security.jwtmanager import JWTManager, get_current_user
from app.security.jwttype import JWTType
from app.services.user_service import UserService 
from app.security.hasher import hash_password



router = APIRouter(
    prefix="/user"
)

@router.post("/registration")
async def reg(request: UserRegistration, session: Session = Depends(get_session)):
    result = await UserService(session).register(request)

    jwt_manager = JWTManager()
    access_token = jwt_manager.encode_token({ "userId": str(result.id) }, token_type=JWTType.ACCESS)
    refresh_token = jwt_manager.encode_token({ "userId": str(result.id) }, token_type=JWTType.REFRESH)
    return AccessToken(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
        
    )


@router.put("/update_profile")
async def update_profile(request: UserUpdate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    request.password = hash_password(request.password)
    result = await UserService(session).update_profile(user.id, request)
    return result

@router.post("/authtorization")
async def profile(username: str = Form(), password: str = Form(), session: Session = Depends(get_session)):
    user = await UserService(session).get_profile(login=username)
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не найден")
    authorized = await UserService(session).authorize(username, password)
    if not authorized:
        raise HTTPException(status_code=401, detail="")
    
    jwt_manager = JWTManager()
    access_token = jwt_manager.encode_token({ "userId": str(user.id) }, token_type=JWTType.ACCESS)
    refresh_token = jwt_manager.encode_token({ "userId": str(user.id) }, token_type=JWTType.REFRESH)
    return AccessToken(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
        
    )
@router.get("/get_profile")
async def me(user: User = Depends(get_current_user)):
    return user



@router.get("/refresh")
async def refresh(token: str = Depends(JWTManager().refresh_access_token)):
    response = JSONResponse(content = {
        "access_token": token
    })
    response.set_cookie(key="access_token", value=token, httponly=True)
    return response