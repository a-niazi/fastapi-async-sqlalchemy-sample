from fastapi import APIRouter, FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
import sys, os
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent)
from controller import note_router, task_router
from fastapi import Request
from database.base import Database

router = APIRouter()

@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
	root_path = req.scope.get("root_path", "").rstrip("/")
	print(req.scope.get("root_path", ""))
	print(root_path)
	openapi_url = root_path + app.openapi_url
	print(openapi_url)
	return get_swagger_ui_html(
		openapi_url=openapi_url,
		title="Appic Apis",
	)


@router.on_event("startup")
async def on_startup():
	database = Database()
	await database.init_db()

router.include_router(note_router)
router.include_router(task_router)

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="localhost", port=8000, log_level="debug")

