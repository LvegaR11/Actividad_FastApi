from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Contracts.user_repository import UserRepository
from app.Domain.Model.user import User
from app.Domain.Schemas.user_schema import UserRequestModel, UserResponseModel


class UserCrud(UserRepository):
  
    @staticmethod
    def create( user: UserRequestModel, db: Session) -> UserResponseModel:

        try:
            _user = db.query(User).filter(User.email == user.email).first()
            if _user:
                raise ValueError(f"El usuario con email  ya existe")
            _user = User(**user.model_dump())
            db.add(_user)
            db.commit()
        
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return UserResponseModel(**_user.model_dump())
    
    @staticmethod
    def get_by_id( id: int, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def get_by_email(email: str, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def find_all(db: Session) -> list[UserResponseModel]:
        try:
            _users = db.query(User).all()
            return [UserResponseModel(**_user.model_dump()) for _user in _users]
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update(id: int, user: UserRequestModel, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def delete(id: int, db: Session) -> None:
        pass    