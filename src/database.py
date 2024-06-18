from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATA_BASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



engine = create_async_engine(DATA_BASE_URL, poolclass = NullPool)
async_session = sessionmaker(autocommit = False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_async_sessioon()-> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session