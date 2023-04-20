from typing import Union

from sqlalchemy import URL, MetaData
from sqlalchemy.ext.asyncio import create_async_engine as sa_create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return sa_create_async_engine(url=url, echo=True, pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata: MetaData) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
