from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    AsyncEngine
)
import os

from app.settings.settings import settings

async def get_engine() -> AsyncEngine:
    return create_async_engine(str(settings.db_url))


async def get_session():

    async_session = sessionmaker(await get_engine(), class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
