from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from core.config import settings

db_url: str = "{sgbd}://{user}:{password}@{server}/{database}".format(
    sgbd=settings.SGBD,
    user=settings.USER,
    password=settings.PASSWORD,
    server=settings.SERVER,
    database=settings.DATABASE,
)

engine: AsyncEngine = create_async_engine(db_url)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine,
)
