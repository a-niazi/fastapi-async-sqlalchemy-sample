# from config import config
# from typing import Generator
# from .base_class import Base
# from collections.abc import AsyncGenerator
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
#
# engine = create_async_engine(config.DB_URI, async_creator=True, future=True, pool_pre_ping=True)
# SessionLocal = async_sessionmaker(engine,
#                                   autocommit=False,
#                                   autoflush=False,
#                                   expire_on_commit=False,
#                                   class_=AsyncSession)
#
#
# async def init_db() -> AsyncGenerator[AsyncSession, None]:
#
#     engine = create_async_engine(config.DB_URI)
#
#     async with engine.begin() as conn:
#         # await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#     # session = async_sessionmaker(engine)()
#     # return session
#     # # await session.close()
#
#
# async def get_db() -> Generator:
#     async with SessionLocal.begin() as db:
#         yield db
#
#
