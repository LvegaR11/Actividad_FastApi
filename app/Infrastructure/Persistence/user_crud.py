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
    def get_by_id(self, id: int, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def get_by_email(self, email: str, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def find_all(self, db: Session) -> list[UserResponseModel]:
        pass

    @staticmethod
    def update(self, id: int, user: UserRequestModel, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def delete(self, id: int, db: Session) -> None:
        pass    