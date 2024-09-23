from models import Task
from typing import List
from controller import schemas
from pydantic import parse_obj_as
from repository import TaskRepository


class TaskService:
	def __init__(self):
		self.task_repository = TaskRepository()

	async def get_by_id(self, task_id: int) -> schemas.Task:
		data = await self.task_repository.get_by_id(task_id)
		return data

	async def get_all(self) -> List[schemas.Task]:
		data = await self.task_repository.get_all()
		return parse_obj_as(List[schemas.Task], data)

	async def add(self, data: schemas.TaskCreate) -> Task:
		return await self.task_repository.add(Task(title=data.title, description=data.description))

	async def delete_note(self, task_id: int):
		await self.task_repository.delete_by_id(task_id)