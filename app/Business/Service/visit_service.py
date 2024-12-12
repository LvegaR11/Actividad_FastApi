from sqlalchemy.orm import Session
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitResponseModel
from app.Infrastructure.Persistence import VisitCrud


class VisitService:

    visit_repository = VisitCrud()

    @classmethod
    def create(self, id: int | None, location: str, duration: float, number_of_persons: int, visit_date: str, user_id: int, db: Session) -> VisitResponseModel:
        visit_response = self.visit_repository.create(VisitRequestModel(id=id, location=location, duration=duration, number_of_persons=number_of_persons, visit_date=visit_date, user_id=user_id), user_id, db)
        return visit_response
    
    @classmethod
    def find_all(self, db: Session) -> list[VisitResponseModel]:
        visits = self.visit_repository.find_all(db)
        return visits
    
    @classmethod
    def delete(self, id: int, db: Session) -> str:
        self.visit_repository.delete(id, db)
        return f"Visita con id {id} eliminado correctamente"