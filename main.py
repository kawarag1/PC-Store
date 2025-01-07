from fastapi import FastAPI, HTTPException
from fastapi import Form
from pydantic import BaseModel
import uvicorn
from requests import post
from database.config import *
from models.models import *
from routing import main_router

app = FastAPI(
    title= "PCStore",
    description="Магазин компьютерной техники",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
app.include_router(main_router.main_router, prefix="/user")


# @app.get("/authtorization/{login}/{password}", summary = "Авторизация пользователей")
# async def auth(login:str, password:str):
#     with DBSettings.get_session() as conn:
#         user = await conn.query(User).filter(User.login == login and User.password == password).first()
#         if user == None:
#             raise HTTPException(status_code=404, detail="User not found")


# @app.get("/profile/{user_id}")
# async def profile(user_id:int):
#     with DBSettings.get_session() as conn:
#         profile = conn.query(User).filter(User.id == user_id).first()

# @app.post("/register/{login}/{password}/{name}/{surname}/{patronymic}/{email}")
# async def refister(login:str, password:str, name:str, surname:str, email:str, patronymic:str = None)









uvicorn.run(app, host="127.0.0.1", port=8000)    