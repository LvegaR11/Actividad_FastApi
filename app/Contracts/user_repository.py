from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.Domain.Schemas.user_schema import UserRequestModel, UserResponseModel, UserToUpdateModel



class UserRepository(ABC):
    @abstractmethod
    def create(self, user: UserRequestModel, db: Session) -> UserResponseModel:
        pass

    @abstractmethod
    def get_by_id(self, id: int, db: Session) -> UserResponseModel:
        pass

    @abstractmethod
    def get_by_email(self, email: str, db: Session) -> UserResponseModel:
        pass

    @abstractmethod
    def find_all(self, db: Session) -> list[UserResponseModel]:
        pass

    @abstractmethod
    def update(self, id: int, user: UserToUpdateModel, db: Session) -> UserResponseModel:
        pass

    @abstractmethod
    def delete(self, id: int, db: Session) -> None:
        pass    