from fastapi import FastAPI, APIRouter
from app.Routers import user_router 

app = FastAPI()

api_v1 = APIRouter(prefix = "/api/v1")
app.include_router(user_router)
app.include_router(api_v1)
