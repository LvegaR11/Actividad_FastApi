from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Domain.Model.user import User
from app.Domain.Model.visit import Visit
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitResponseModel, VisitToUpdateModel
from app.Contracts.visit_repository import VisitRepository



class VisitCrud (VisitRepository):

    @staticmethod
    def create(visit: VisitRequestModel, user_id: int, db: Session) -> VisitResponseModel:
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError(f"No existe el usuario con id {visit.user_id}")
            
            existing_visit = db.query(Visit).filter(Visit.id == visit.id).first()
            if existing_visit:
                raise ValueError(f"La visita con id {visit.id} ya existe")
            
            _visit = Visit(**visit.model_dump())
            db.add(_visit)
            db.commit()
            db.refresh(_visit)
        
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
       
        return VisitResponseModel(**_visit.model_dump())
    
    @staticmethod 
    def get_by_user_id(user_id: int, db: Session) -> list[VisitResponseModel]:
        try:
            _visits = db.query(Visit).filter(Visit.user_id == user_id).all()
            if not _visits:
                raise ValueError(f"No existe ninguna visita con el usuario con id {user_id}")
            return [VisitResponseModel(**_visit.model_dump()) for _visit in _visits]
        
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        except Exception as e:
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

    @staticmethod
    def update(id: int, visit: VisitToUpdateModel, db: Session) -> VisitResponseModel:
        try:
            _visit = db.query(Visit).filter(Visit.id == id).first()
            if not _visit:
                raise ValueError(f"No existe la visita con id {id}")
            _visit.location = visit.location if visit.location else _visit.location
            _visit.duration = visit.duration if visit.duration else _visit.duration
            _visit.number_of_persons = visit.number_of_persons if visit.number_of_persons else _visit.number_of_persons
            _visit.visit_date = visit.visit_date if visit.visit_date else _visit.visit_date
            db.commit()
            return VisitResponseModel(**_visit.model_dump())
        
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))