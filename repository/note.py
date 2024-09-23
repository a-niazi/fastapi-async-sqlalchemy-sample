from .base import BaseRepository
from controller import schemas
from datetime import datetime
from sqlalchemy import func
from models import Note


class NoteRepository(BaseRepository):
	def __init__(self):
		super().__init__()
		self.model = Note

	async def update_by_id(self, note_id: int, title: str = None, note: str = None):
		async with self.database.async_session() as session:
			async with session.begin():
				note_item = await session.get(Note, note_id)
				if note_item:
					if title:
						note_item.title = title
					if note:
						note_item.note = note
					note_item.updated_at = datetime.now()
					await session.commit()

	async def add(self, data: schemas.NoteCreate) -> Note:
		async with self.database.async_session() as session:
			async with session.begin():
				note = Note(
					title=data.title,
					note=data.note,
				)
				session.add(note)
			await session.commit()
		return note
