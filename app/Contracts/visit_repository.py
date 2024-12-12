from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitResponseModel

class VisitRepository(ABC):
    @abstractmethod
    def create(self, visit: VisitRequestModel, user_id: int, db: Session) -> VisitResponseModel:
        pass

   
    @abstractmethod
    def find_all(self, db: Session) -> list[VisitResponseModel]:
        pass
 
  
    @abstractmethod
    def delete(self, id: int, db: Session) -> None:
        pass

