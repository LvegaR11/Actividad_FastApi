from pydantic import BaseModel, Field, validator
from datetime import datetime

class VisitRequestModel(BaseModel):
    id: int | None = None
    location: str 
    duration: float 
    number_of_persons: int 
    visit_date: str
    user_id: int 

    class Config:
        json_schema_extra = {
            'example': {
                'location': 'casa',
                'duration': 10,
                'number_of_persons': 2,
                'visit_date': '2023-01-01',
                'user_id': 1
            }
        }


class VisitResponseModel(BaseModel):

    location: str
    duration: float
    number_of_persons: int
    visit_date: str
    user_id: int

    class Config:
        pass
