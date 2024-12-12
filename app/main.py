from fastapi import FastAPI, APIRouter
from app.Routers import user_router, visit_router 

app = FastAPI()

api_v1 = APIRouter(prefix = "/api/v1")
app.include_router(user_router)
app.include_router(api_v1)

app_2 = APIRouter(prefix = "/api/v2")
app.include_router(visit_router)
app.include_router(app_2)
