from app.services.search_service import *

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix = "/search"
)

@router.get("/get_all_products")
async def get_products(session: AsyncSession = Depends(get_session), word: str | None = None):
    result = await SearchService(session).get_all_products()
    return result