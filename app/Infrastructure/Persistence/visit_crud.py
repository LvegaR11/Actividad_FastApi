from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Domain.Model.visit import Visit
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitResponseModel
from app.Contracts.visit_repository import VisitRepository



class VisitCrud (VisitRepository):

    @staticmethod
    def create(visit: VisitRequestModel, db: Session) -> VisitResponseModel:
        try:
            _visit = db.query(Visit).filter(Visit.location == visit.location).first()
            if _visit:
                raise ValueError(f"La visita con location {visit.location} ya existe")
            _visit = Visit(**visit.model_dump())
            db.add(_visit)
            db.commit()
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return VisitResponseModel(**_visit.model_dump())
    
    @staticmethod
    def find_all(db: Session) -> list[VisitResponseModel]:
        try:
            _visits = db.query(Visit).all()
            return [VisitResponseModel(**_visit.model_dump()) for _visit in _visits]
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    @staticmethod
    def delete(id: int, db: Session) -> None:
        try:
            _visit = db.query(Visit).filter(Visit.id == id).first()
            if not _visit:
                raise ValueError(f"No existe la visita con id {id}")
            db.delete(_visit)
            db.commit()
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
