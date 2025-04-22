from datetime import timedelta
import datetime
from typing import Optional, Union
from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer

from jwt import encode, decode


from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_service import UserService
from app.settings.settings import settings
from app.models.models import User
from app.database.connector import get_session

from app.security.hasher import verify_password
from app.security.jwttype import JWTType

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/user/authtorization")

async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)) -> User:
    

    payload = JWTManager().decode_token(token)
    if isinstance(payload, str):
        raise HTTPException(
            status_code=401,
            detail=payload,
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    username: str = payload["userId"]
    if username is None:
        raise HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    
    user = await UserService(session).get_profile(id=int(username))
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

class JWTManager:

    def __init__(self):
        self.SECRET_KEY = settings.JWT_SECRET_KEY
        self.ALGORITHM = settings.JWT_ALGORITHM
        self.ACCESS_TOKEN_LIFETIME = settings.JWT_ACCESS_TOKEN_LIFETIME_MINUTES
        self.REFRESH_TOKEN_LIFETIME = settings.JWT_REFRESH_TOKEN_LIFETIME_HOURS

    def encode_token(self, payload: dict, token_type: JWTType = JWTType.ACCESS):
        jwt_payload = payload.copy()

        current_time = datetime.datetime.now()
        expire = timedelta(minutes=self.ACCESS_TOKEN_LIFETIME) if token_type == JWTType.ACCESS else timedelta(hours=self.REFRESH_TOKEN_LIFETIME)
        jwt_payload.update({"exp": current_time + expire})
        return encode(jwt_payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
    
    def decode_token(self, token: str) -> Union[dict, str]:
        try:
            return decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        except:
            return "Invalid token"
        
    async def refresh_access_token(self, token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)):
        if not token:
            raise HTTPException(status_code=400, detail="Refresh token is not provided")
        
        token_data = self.decode_token(token)
        if isinstance(token_data, str):
            raise HTTPException(status_code=400, detail=token_data)

        user = await UserService(session).get_profile(id=int(token_data["userId"]))

        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        
        return self.encode_token({ "userId": str(user.id) }, token_type=JWTType.ACCESS)