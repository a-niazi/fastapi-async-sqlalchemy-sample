from models import *
from config import config
from database.base_class import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from typing import Optional


class Database:
	engine: Optional[AsyncEngine] = None
	async_session: Optional[sessionmaker] = None

	@classmethod
	def init_engine(self, db_url: str):
		if self.engine is None:
			self.engine = create_async_engine(db_url, echo=True)
			self.async_session = sessionmaker(
				bind=self.engine,
				expire_on_commit=False,
				class_=AsyncSession
			)

	@classmethod
	async def get_session(self):
		if self.engine is None or self.async_session is None:
			raise Exception("Engine is not initialized. Call 'init_engine' first.")
		"""Context manager to provide an async session."""
		async with self.async_session() as session:
			yield session

	@classmethod
	async def init_db(self):
		"""Initialize the database by creating all tables."""
		async with self.engine.begin() as conn:
			await conn.run_sync(Base.metadata.create_all)

	async def close(self):
		"""Dispose of the engine."""
		await self.engine.dispose()

