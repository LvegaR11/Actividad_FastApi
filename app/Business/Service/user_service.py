
from sqlalchemy.orm import Session
from app.Domain.Schemas.user_schema import UserRequestModel, UserResponseModel
from app.Infrastructure.Persistence import UserCrud


class UserService:

    user_repository = UserCrud()

    @classmethod
    def create(self, user: UserRequestModel, db: Session) -> UserResponseModel:
        user_response = self.user_repository.create(user, db)
        return user_response

    @classmethod
    def find_all(self, db: Session) -> list[UserResponseModel]:
        users = self.user_repository.find_all(db)
        return users