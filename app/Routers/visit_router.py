from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.Domain.Schemas.visit_schema import VisitRequestModel, VisitToUpdateModel
from app.Infrastructure.Database import get_db
from app.Business.Service.visit_service import VisitService
from fpdf import FPDF
from fastapi.responses import StreamingResponse
from io import BytesIO


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


@visit_router.get("", status_code=status.HTTP_200_OK)
async def get_all_visits(db: Session = Depends(get_db)):
    visits = VisitService.find_all(db)
    return visits

@visit_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_visit(id: int, db: Session = Depends(get_db)):
    response = VisitService.delete(id, db)
    return response

@visit_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_visit(id: int, visit: VisitToUpdateModel, db: Session = Depends(get_db)):
    visit_response = VisitService.update(id, visit, db)
    return visit_response

@visit_router.get("/pdf/", status_code=status.HTTP_200_OK)
async def get_pdf(user_id: int, db: Session = Depends(get_db)):
    visits = VisitService.get_by_user_id(user_id, db)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Reporte de Visitas del usuario', 0, 0, 'C')
    pdf.ln(20)

    for visit in visits:
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f'Id visita: {visit.id}', 0, 1,)
        pdf.cell(0, 10, f'Ubicación: {visit.location}', 0, 1)
        pdf.cell(0, 10, f'Duración: {visit.duration} mins', 0, 1)
        pdf.cell(0, 10, f'Número de Personas: {visit.number_of_persons}', 0, 1)
        pdf.cell(0, 10, f'Fecha: {visit.visit_date}', 0, 1)
        pdf.ln(5)

    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=visitas.pdf"
        }
    )