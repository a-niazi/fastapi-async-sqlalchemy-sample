from datetime import datetime
from typing import List

from fastapi.logger import logger
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession

from controller import schemas
# from app.controllers import note_controller
from models import Note
from utils import helpers
from repository import NoteRepository


class NoteService:
	def __init__(self):
		self.note_repository = NoteRepository()

	async def get_by_id(self, note_id: int) -> schemas.Note:
		data = await self.note_repository.get_by_id(note_id)
		return data

	async def get_all(self) -> List[schemas.Note]:
		data = await self.note_repository.get_all()
		return parse_obj_as(List[schemas.Note], data)

	async def add(self, data: schemas.NoteCreate) -> Note:
		return await self.note_repository.add(Note(title=data.title, note=data.note))

	async def update_note(self, data: schemas.NoteUpdate) -> Note:

		note = await self.note_repository.update_by_id(
			data.id,
			title=data.title,
			note=data.note
		)
		# note = await self.note_repository.get_by_id(data.id)
		#
		# try:
		# 	note.title = data.title
		# 	note.note = data.note
		# 	note.updated_at = datetime.now()
		#
		# 	await helpers.flush_database()
		# except Exception as e:
		# 	logger.error(e)
		# 	raise RuntimeError("Can not update note")

		return note

	async def delete_note(self, note_id: int):
		await self.note_repository.delete_by_id(note_id)

	def _validate_data(self, data: schemas.NoteBase):
		data.title = data.title.strip()
		if len(data.title) < 2:
			raise RuntimeError("The name is too short")

		if len(data.title) > 254:
			raise RuntimeError("The name is too long")