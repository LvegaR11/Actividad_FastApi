from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitResponseModel, VisitToUpdateModel

class VisitRepository(ABC):
    @abstractmethod
    def create(self, visit: VisitRequestModel, user_id: int, db: Session) -> VisitResponseModel:
        pass

   
    @abstractmethod
    def get_by_user_id(self, user_id: int, db: Session) -> list[VisitResponseModel]:
        pass
 
  
    @abstractmethod
    def delete(self, id: int, db: Session) -> None:
        pass

    @abstractmethod
    def update(self, id: int, visit: VisitToUpdateModel , db: Session) -> VisitResponseModel:
        pass

