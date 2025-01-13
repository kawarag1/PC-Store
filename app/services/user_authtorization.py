from app.models.models import User
from app.schemas.requests.user_schema import UserAuth
from app.database.connector import *
from app.security.hasher import verify_password

from sqlalchemy import select
from fastapi import HTTPException



class UserAuthtorization():
    def __init__(self, session:Session):
        self.session = session

    async def authtorization(self, login:str, password:str):
        query = select(User).filter(User.login == login)
        
        
        result = self.session.execute(query)
        user:UserAuth = result.scalars().first()
        
        if user is None:
            raise HTTPException(404, "User is not found")
        else:
            verify = verify_password(password, user.password)
            if verify == False:
                raise HTTPException(404, "Wrong password")
            
            else:
                return user