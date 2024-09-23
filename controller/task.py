from . import schemas
from typing import Annotated
from service import TaskService
from fastapi.logger import logger
from fastapi import APIRouter, Response, HTTPException, status, Depends

router = APIRouter()


@router.get("/tasks")
async def get_all(task_service: Annotated[TaskService, Depends(TaskService)]):
	try:
		data = await task_service.get_all()
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.get("/tasks/{task_id}")
async def get_by_id(
		task_service: Annotated[TaskService, Depends(TaskService)],
		note_id: int):
	try:
		data = await task_service.get_by_id(note_id)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.post("/tasks")
async def add(
		task_service: Annotated[TaskService, Depends(TaskService)],
		body: schemas.TaskCreate):
	try:
		data = await task_service.add(body)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return data


@router.delete("/tasks/{task_id}")
async def delete(
		task_service: Annotated[TaskService, Depends(TaskService)],
		note_id: int):
	try:
		await task_service.delete_note(note_id)
	except Exception as e:
		logger.error(e)
		raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
	return Response(status_code=status.HTTP_204_NO_CONTENT)
