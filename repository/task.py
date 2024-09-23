from .base import BaseRepository
from controller import schemas
from models import Task


class TaskRepository(BaseRepository):
	def __init__(self):
		super().__init__()
		self.model = Task

	async def update(self, task_id: int, title: str = None, note: str = None):
		async with self.database.async_session() as session:
			async with session.begin():
				task = await session.get(Task, task_id)
				if task:
					if title:
						task.title = title
					if note:
						task.description = note
					await session.commit()
	
	async def add(self, data: schemas.TaskCreate) -> Task:
		async with self.database.async_session() as session:
			async with session.begin():
				task = Task(
					title=data.title,
					description=data.description,
				)
				session.add(task)
			await session.commit()
		return task
