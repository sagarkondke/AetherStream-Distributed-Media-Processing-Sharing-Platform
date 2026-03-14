from collections.abc import AsyncGenerator
import uuid


from sqlalchemy import Column , String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship

DATABASE_URL='sqlite+aiosqlite:///./test.db'

class post(DeclarativeBase):
    __table__='post'

    id= Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    caption =Column(Text)
    url =Column (String, nullable=False)
    file_name= Column(DateTime, default=DateTime.utcnow)

engine =create_async_engine(DATABASE_URL)
async_session_maker =async_sessionmaker(engine,expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_aync(DeclarativeBase.metadata.create_all)


async def get_async_session() ->AsyncGenerator[AsyncSession,None]:
    async with async_session_maker() as session:
        yield session
