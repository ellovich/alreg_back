from sqlalchemy import Column, Date, DateTime, Integer, NullPool, String, func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = { "poolclass": NullPool }
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
async_session_maker =  sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class BaseAlchemyModel(DeclarativeBase):
    id = Column(Integer, primary_key=True, nullable=False, index=True, unique=True)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())
