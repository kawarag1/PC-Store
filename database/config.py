from sqlalchemy import *
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

class DBSettings():
        @staticmethod
        def get_session():
            load_dotenv()
            engine = create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}")
            # engine = create_engine(f"postgresql+psycopg2://postgres:postgres@localhost:5555/CourseProject")
            return Session(bind=engine)
        
