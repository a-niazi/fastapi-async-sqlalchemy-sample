from . import schemas
from typing import Annotated
from service import NoteService
from fastapi.logger import logger
from fastapi import APIRouter, Response, HTTPException, status, Depends

router = APIRouter()


@router.get("/notes")
async def get_all(note_service: Annotated[NoteService, Depends(NoteService)]):
	try:
		data = await note_service.get_all()
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.get("/notes/{note_id}")
async def get_by_id(
		note_service: Annotated[NoteService, Depends(NoteService)],
		note_id: int):
	try:
		data = await note_service.get_by_id(note_id)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.post("/notes")
async def add(
		note_service: Annotated[NoteService, Depends(NoteService)],
		body: schemas.NoteCreate):
	try:
		data = await note_service.add(body)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.put("/notes")
async def update(
	note_service: Annotated[NoteService, Depends(NoteService)],
	body: schemas.NoteUpdate):
	try:
		data = await note_service.update_note(body)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.delete("/notes/{note_id}")
async def delete(
		note_service: Annotated[NoteService, Depends(NoteService)],
		note_id: int):
	try:
		await note_service.delete_note(note_id)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return Response(status_code=status.HTTP_204_NO_CONTENT)
