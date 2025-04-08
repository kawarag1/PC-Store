from app.security.jwtmanager import get_current_user
from app.services.search_service import *

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix = "/search"
)

@router.get("/get_all_products")
async def get_products(session: AsyncSession = Depends(get_session), word: str | None = None, user: User = Depends(get_current_user)):
    result = await SearchService(session).get_all_products()
    return result

@router.get("/get_filter_products")
async def get_filter_products(filter:str, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    result = await SearchService(session).get_filter_products(filter)
    return result