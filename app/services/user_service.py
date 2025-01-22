from typing import Union
from app.models.models import User
from app.schemas.request.user.user_auth_schema import UserAuth
from app.schemas.request.user.user_registration_schema import UserRegistration
from app.schemas.request.user.user_update_schema import UserUpdate
from app.database.connector import *
from app.security.hasher import hash_password
from app.security.hasher import verify_password


from sqlalchemy import select
from fastapi import HTTPException



class UserService():
    def __init__(self, session: Session):
        self.session = session

    async def get_profile(self, **kwargs):
        query = select(User).filter_by(**kwargs)

        result = self.session.execute(query)
        return result.scalars().first()
    
    async def register(self, request: UserRegistration):
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
    
    async def update_profile(self, user_id: int, data: UserUpdate):
        data_dict = data.dict(exclude_unset=True)

        update_fileds = {}
        for key, value in data_dict.items():
            if value is not None:
                update_fileds[key] = value

        if not update_fileds:
            return None
        query = update(User).filter(User.id == user_id).values(data_dict).returning(User)
        '''
        оказывается можно в боди оставить только 1 нужное поле и всё, на мобилке это реализовать можно через создание
        джсон словарика...
        '''
        result = self.session.execute(query)
        self.session.commit()
        
        
        return result.scalars().first()


    async def authorize(self, login: str, password: str):
        authenticated = await self.authenticate_user(login, password)
        if isinstance(authenticated, str):
            raise HTTPException(
                status_code = 401,
                detail = "Неправильный логин или пароль"
            )
        return authenticated
        

    async def authenticate_user(self, login: str, password: str) -> Union[User, str]:
        user = await UserService(self.session).get_profile(login=login)
        if not user:
            return ("User not found")
        if not verify_password(password, user.password):
            return ("Invalid password")
        return (user)
