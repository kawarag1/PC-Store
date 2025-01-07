from sqlalchemy import *
from sqlalchemy.orm import Session
import os

from app.settings.settings import settings


def get_session():
    engine = create_engine(str(settings.db_url))
    return Session(bind=engine)
