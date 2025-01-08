from sqlalchemy import *
from sqlalchemy.orm import Session
import os

from app.settings.settings import settings


def get_session():
    engine = settings.db_url
    return Session(bind=str(engine))
