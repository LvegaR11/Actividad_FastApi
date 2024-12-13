from io import BytesIO
from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse
from fpdf import FPDF
from sqlalchemy.orm import Session
from app.Domain.Schemas.user_schema import UserRequestModel, UserToUpdateModel
from app.Infrastructure.Database import get_db
from app.Business.Service.user_service import UserService



user_router = APIRouter(
    prefix = "/user",
    tags=["user"]
)


@user_router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequestModel, db: Session = Depends(get_db)):
    user_response = UserService.create(user, db)
    return user_response

@user_router.get("", status_code=status.HTTP_200_OK)
async def find_all_users(db: Session = Depends(get_db)):
    users = UserService.find_all(db)
    return users

@user_router.get("/{id}", status_code=status.HTTP_200_OK)
async def find_user_by_id(id: int, db: Session = Depends(get_db)):
    user = UserService.user_by_id(id, db)
    return user

@user_router.get("/{email}", status_code=status.HTTP_200_OK)
async def find_user_by_email(email: str, db: Session = Depends(get_db)):
    user = UserService.user_by_email(email, db)
    return user

@user_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, db: Session = Depends(get_db)):
    response = UserService.delete(id, db)
    return response

@user_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_user(id: int, user: UserToUpdateModel, db: Session = Depends(get_db)):
    user_response = UserService.update(id, user, db)
    return user_response

@user_router.get("/pdf/", status_code=status.HTTP_200_OK)
async def get_pdf(db: Session = Depends(get_db)):
    users = UserService.get_pdf(db)
    if not users:  
        return {"detail": "No se encontraron usuarios para generar el reporte"}

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Reporte de usuarios', 0, 0, 'C')
    pdf.ln(20)


    for user in users:
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f'ID: {user.id}', 0, 1)
        pdf.cell(0, 10, f'Nombre: {user.name}', 0, 1)
        pdf.cell(0, 10, f'Apellido: {user.last_name}', 0, 1)
        pdf.cell(0, 10, f'Role: {user.role}', 0, 1)
        pdf.cell(0, 10, f'Email: {user.email}', 0, 1)
        pdf.cell(0, 10, f'Teléfono: {user.phone}', 0, 1)
        pdf.cell(0, 10, f'Estado: {user.status}', 0, 1)
        pdf.ln(5)

    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=Usuarios.pdf"
        }
    )