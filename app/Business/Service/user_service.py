
from sqlalchemy.orm import Session
from app.Domain.Schemas.user_schema import UserRequestModel, UserResponseModel, UserToUpdateModel
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
    
    @classmethod
    def delete(self, id: int, db: Session) -> str:
        self.user_repository.delete(id, db)
        return f"Usuario con id {id} eliminado correctamente"
    
    @classmethod
    def user_by_email(self, email: str, db: Session) -> UserResponseModel:
        user = self.user_repository.get_by_email(email, db)
        return user
    
    @classmethod
    def user_by_id(self, id: int, db: Session) -> UserResponseModel:
        user = self.user_repository.get_by_id(id, db)
        return user
    @classmethod
    def update(self, id: int, user: UserToUpdateModel, db: Session) -> UserResponseModel:
        user_response = self.user_repository.update(id, user, db)
        return user_response