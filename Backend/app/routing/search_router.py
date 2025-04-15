from app.security.jwtmanager import get_current_user
from app.services.search_service import *

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix = "/search"
)

@router.get("/get_all_products")
async def get_products(session: AsyncSession = Depends(get_session)):
    result = await SearchService(session).get_all_products()
    return result

@router.get("/get_filter_products")
async def get_filter_products(filter:str, session: AsyncSession = Depends(get_session)):
    result = await SearchService(session).get_filter_products(filter)
    return result


@router.get("/get_products_with_word")
async def get_products_with_word(word: str, session: AsyncSession = Depends(get_session)):
    result = await SearchService(session).get_products_with_word(word)
    return result