from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncAttrs,
)
# from models import Phonebook, Contact
from sqlalchemy.orm import DeclarativeBase
from phoonbook_service.src.config import dsn

async_engine = create_async_engine(url=dsn, echo=True)
print(dsn)
async_session_factory = async_sessionmaker(async_engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
