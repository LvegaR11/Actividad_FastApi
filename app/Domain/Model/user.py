from app.Infrastructure.Database import Base
from datetime import datetime
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column, Mapped


class User(Base):
        __tablename__ = 'user'
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        password: Mapped[str] = mapped_column(String(50))
        name: Mapped[str] = mapped_column(String(50))
        last_name: Mapped[str] = mapped_column(String(50))
        role: Mapped[str] = mapped_column(String(50))
        email: Mapped[str] = mapped_column(String(256), unique=True)
        phone: Mapped[str] = mapped_column(String(50))
        status: Mapped[str] = mapped_column(String(50))
        created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now())

        def model_dump(self):
                return {
                    'id': self.id,
                    'name': self.name,
                    'last_name': self.last_name,
                    'role': self.role,
                    'email': self.email,
                    'phone': self.phone,
                    'status': self.status,
                    'created_at': self.created_at.__str__()
                }
