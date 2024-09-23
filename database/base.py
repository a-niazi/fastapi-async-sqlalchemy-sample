from models import *
from config import config
from database.base_class import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class Database:
	def __init__(self):
		# Create the async engine
		self.engine = create_async_engine(config.DB_URI, echo=True)
		# Create an async session maker
		self.async_session = sessionmaker(
			bind=self.engine,
			class_=AsyncSession,
			expire_on_commit=False
		)

	async def init_db(self):
		"""Initialize the database by creating all tables."""
		async with self.engine.begin() as conn:
			await conn.run_sync(Base.metadata.create_all)

	async def close(self):
		"""Dispose of the engine."""
		await self.engine.dispose()

	async def get_session(self):
		"""Context manager to provide an async session."""
		async with self.async_session() as session:
			yield session
