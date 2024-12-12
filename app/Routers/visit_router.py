from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitToUpdateModel
from app.Infrastructure.Database import get_db
from app.Business.Service.visit_service import VisitService

visit_router = APIRouter(
    prefix = "/visit",
    tags=["visit"]
)

@visit_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_visit(visit_request: VisitRequestModel, db: Session = Depends(get_db)):
    visit_service = VisitService()
    visit_response = visit_service.create(visit_request.id, visit_request.location, visit_request.duration, 
                                          visit_request.number_of_persons, visit_request.visit_date, 
                                          visit_request.user_id, db)
    return visit_response

@visit_router.get("/visit/{user_id}", status_code=status.HTTP_200_OK)
async def get_visits_by_user_id(user_id: int, db: Session = Depends(get_db)):
    visits = VisitService.get_by_user_id(user_id, db)
    return visits

@visit_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_visit(id: int, db: Session = Depends(get_db)):
    response = VisitService.delete(id, db)
    return response

@visit_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_visit(id: int, visit: VisitToUpdateModel, db: Session = Depends(get_db)):
    visit_response = VisitService.update(id, visit, db)
    return visit_response