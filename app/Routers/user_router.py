from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.Domain.Schemas.user_schema import UserRequestModel
from app.Infrastructure.Database import get_db
from app.Business.Service.user_service import UserService



user_router = APIRouter(
    prefix = "/user",
    tags=["user"]
)


@user_router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequestModel, db: Session = Depends(get_db)):
    user_response = UserService.create(user, db)
    return user_response

