from app.models.models import User
from app.schemas.requests.user_schema import UserRequest
from app.database.connector import *
from sqlalchemy import select

class UserProfile():
    def __init__(self, session:Session):
        self.session = session

    async def get_profile(self, login:str):
        query = select(User).filter(User.login == login)

        result = self.session.execute(query)
        return result.scalars().first()
