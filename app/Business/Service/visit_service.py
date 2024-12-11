from sqlalchemy.orm import Session
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitResponseModel
from app.Infrastructure.Persistence import VisitCrud


class VisitService:

    visit_repository = VisitCrud()

    @classmethod
    def create(self, visit: VisitRequestModel, db: Session) -> VisitResponseModel:
        visit_response = self.visit_repository.create(visit, db)
        return visit_response

    @classmethod
    def find_all(self, db: Session) -> list[VisitResponseModel]:
        visits = self.visit_repository.find_all(db)
        return visits
    
    @classmethod
    def delete(self, id: int, db: Session) -> str:
        self.visit_repository.delete(id, db)
        return f"Visita con id {id} eliminado correctamente"