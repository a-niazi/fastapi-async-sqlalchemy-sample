import sys
from typing import List
from typing import Generator
from sqlalchemy import select
from database.base import Database


class BaseRepository:
	def __init__(self):
		self.database = Database()
		self.model = None

	async def execute_stmt(self, stmt, first_only=False):
		async with self.database.async_session() as session:
			result = await session.execute(stmt)
		if first_only:
			return result.scalar_one_or_none()
		return result.scalars().all()

	async def get_all(self) -> List[Generator]:
		items = await self.execute_stmt(select(self.model))
		if items is None:
			return []
		return items

	async def get_by_id(self, id: int) -> Generator:
		return await self.execute_stmt(select(self.model).filter_by(id=id))

	async def delete_by_id(self, id: int):
		try:
			async with self.database.async_session() as session:
				async with session.begin():
					item = await session.get(self.model, id)
					if item:
						await session.delete(item)
						await session.commit()
		except Exception as e:
			raise RuntimeError("Can not delete the note")

	async def add(self, data) -> Generator:
		async with self.database.async_session() as session:
			async with session.begin():
				session.add(data)
			await session.commit()
		return data
