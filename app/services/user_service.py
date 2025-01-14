from app.models.models import User
from app.schemas.request.user.user_auth_schema import UserAuth
from app.schemas.request.user.user_registration_schema import UserRequest
from app.database.connector import *
from app.security.hasher import hash_password
from app.security.hasher import verify_password


from sqlalchemy import select
from fastapi import HTTPException



class UserService():
    def __init__(self, session: Session):
        self.session = session

    async def authtorization(self, login: str, password: str):
        query = select(User).filter(User.login == login)
        
        
        result = self.session.execute(query)
        user:UserAuth = result.scalars().first()
        
        if user is None:
            raise HTTPException(
                status_code = 404,
                detail = "User is not found"
                )
        if not verify_password(password, user.password):
            raise HTTPException(
                status_code = 404,
                detail = "Wrong password"
                )        
        return user
    

    async def get_profile(self, login: str):
        query = select(User).filter(User.login == login)

        result = self.session.execute(query)
        return result.scalars().first()
    
    async def register(self, request: UserRequest):
        query = (
            insert(User)
            .values(
                login=request.login,
                password=hash_password(request.password),
                email=request.email,
                name=request.name,
                surname=request.surname,
                patronymic=request.patronymic
            )
            .returning(User)
        )

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().first()