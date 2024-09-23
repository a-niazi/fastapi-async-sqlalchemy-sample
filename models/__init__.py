from database.base_class import Base
# from database.session import SessionLocal, engine
from .note import Note
from .task import Task
import asyncio

# Base.metadata.create_all(engine, tables=[Note])


# async def init_models():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
# asyncio.run(init_models())

# Base.metadata.create_all(engine)


# async def init_db():
#     # async with engine.begin() as conn:
#     #     # await conn.run_sync(SQLModel.metadata.drop_all)
#     #     await conn.run_sync(Base.metadata.create_all)
#     async with SessionLocal() as session:
#         conn = await session.connection()
#         # await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)