from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.Domain.Schemas.user_schema import UserRequestModel, UserToUpdateModel
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

@user_router.get("", status_code=status.HTTP_200_OK)
async def find_all_users(db: Session = Depends(get_db)):
    users = UserService.find_all(db)
    return users

@user_router.get("/{id}", status_code=status.HTTP_200_OK)
async def find_user_by_id(id: int, db: Session = Depends(get_db)):
    user = UserService.user_by_id(id, db)
    return user

@user_router.get("/{email}", status_code=status.HTTP_200_OK)
async def find_user_by_email(email: str, db: Session = Depends(get_db)):
    user = UserService.user_by_email(email, db)
    return user

@user_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, db: Session = Depends(get_db)):
    response = UserService.delete(id, db)
    return response

@user_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_user(id: int, user: UserToUpdateModel, db: Session = Depends(get_db)):
    user_response = UserService.update(id, user, db)
    return user_response


