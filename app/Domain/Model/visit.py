from app.Infrastructure.Database import Base
from datetime import datetime
from sqlalchemy import DateTime, Integer, String, FLOAT, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.Domain.Model.user import User

class Visit(Base):
    __tablename__ = 'visit'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), index=True)
    location: Mapped[str] = mapped_column(String(50))
    duration: Mapped[float] = mapped_column(FLOAT)
    number_of_persons: Mapped[int] = mapped_column(Integer)
    visit_date: Mapped[str] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    use: Mapped['User'] = relationship() 

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
