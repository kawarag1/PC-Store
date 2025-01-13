from app.models.models import User
from app.schemas.requests.user_schema import UserRequest
from app.database.connector import *
from app.security.hasher import hash_password

from sqlalchemy import insert

class UserRegister:
    def __init__(self, session: Session):
        self.session = session

    async def register(self, request: UserRequest):
        password = hash_password(request.password)
        query = (
            insert(User)
            .values(
                login=request.login,
                password=password,
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

