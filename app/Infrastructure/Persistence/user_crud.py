from fpdf import FPDF
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.Contracts.user_repository import UserRepository
from app.Domain.Model.user import User
from app.Domain.Schemas.user_schema import UserRequestModel, UserResponseModel


class UserCrud(UserRepository):
  
    @staticmethod
    def create( user: UserRequestModel, db: Session) -> UserResponseModel:

        try:
            _user = db.query(User).filter(User.email == user.email).first()
            if _user:
                raise ValueError(f"El usuario con email  ya existe")
            _user = User(**user.model_dump())
            db.add(_user)
            db.commit()
        
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
        return UserResponseModel(**_user.model_dump())
    
    @staticmethod
    def get_by_id( id: int, db: Session) -> UserResponseModel:
        try:
            _user = db.query(User).filter(User.id == id).first()
            if not _user:
                raise ValueError(f"No existe el usuario con id {id}")
            return UserResponseModel(**_user.model_dump())
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def get_by_email(email: str, db: Session) -> UserResponseModel:
        try:
            _user = db.query(User).filter(User.email == email).first()
            if not _user:
                raise ValueError(f"No existe el usuario con email {email}")
            return UserResponseModel(**_user.model_dump())
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def find_all(db: Session) -> list[UserResponseModel]:
        try:
            _users = db.query(User).all()
            return [UserResponseModel(**_user.model_dump()) for _user in _users]
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update(id: int, user: UserRequestModel, db: Session) -> UserResponseModel:
        try:
            _user = db.query(User).filter(User.id == id).first()
            if not _user:
                raise ValueError(f"No existe el usuario con id {id}")
            _user.name = user.name if user.name else _user.name
            _user.last_name = user.last_name if user.last_name else _user.last_name
            _user.role = user.role if user.role else _user.role
            _user.email = user.email if user.email else _user.email
            _user.phone = user.phone if user.phone else _user.phone
            _user.status = user.status if user.status else _user.status
            db.commit()
            return UserResponseModel(**_user.model_dump())
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def delete(id: int, db: Session) -> None:
        try: 
            _user = db.query(User).filter(User.id == id).first()
            if not _user:
                raise ValueError(f"No existe el usuario con id {id}")
            db.delete(_user)
            db.commit()
        except ValueError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    @staticmethod
    def get_pdf(db: Session) -> bytes:
        try:
            _users = db.query(User).all()
            if not _users:
                raise ValueError(f"No existen usuarios")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(40, 10, 'Usuarios', 0, 0, 'C')
            pdf.ln(20)
            for user in _users:
                pdf.set_font('Arial', '', 12)
                pdf.cell(40, 6, f'Usuario: {user.id} - {user.name} - {user.last_name} - {user.role} - {user.email} - {user.phone} - {user.status}', 0, 0, 'L')
                pdf.ln(10)
            return _users
        
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))