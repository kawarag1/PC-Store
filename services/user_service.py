from models.models import User
from schemas.requests import user_schema
from database.config import *

def profile(user_id:int):
    with DBSettings.get_session() as conn:
        profile = conn.query(User).filter(User.id == user_id).first()
    return profile


def registration(data: user_schema.UserRequest):
    with DBSettings.get_session() as conn:
        user = User(login = data.login, password = data.password, email = data.email, name = data.name, surname = data.surname, patronymic = data.patronymic)

        try:
            conn.add(user)
            conn.commit()
            conn.refresh()

        except Exception as e:
            print(e)

