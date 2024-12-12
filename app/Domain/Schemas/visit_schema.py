from pydantic import BaseModel, ConfigDict, Field, validator
from datetime import datetime

class VisitRequestModel(BaseModel):
    id: int | None = None
    location: str 
    duration: float 
    number_of_persons: int 
    visit_date: str
    user_id: int 

    @classmethod
    def validate_location(cls, location: str) -> str:
       if len(location) < 3:
           raise ValueError('Location must be at least 3 characters long')
       if len(location) > 50:
           raise ValueError('Location must be at most 50 characters long')
       return location
    model_config = ConfigDict(json_schema_extra={
        'example': {
            'location': 'casa',
            'duration': 10,
            'number_of_persons': 2,
            'visit_date': '2023-01-01', 
            'user_id': 1
            }
        })
    

class VisitResponseModel(BaseModel):

    location: str
    duration: float
    number_of_persons: int
    visit_date: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class VisitToUpdateModel(BaseModel):
    location: str | None = None
    duration: float | None = None
    number_of_persons: int | None = None
    visit_date: str | None = None
    
    model_config = ConfigDict(json_schema_extra={
        'example': {
                'location': None,
                'duration': None,
                'number_of_persons': None,
                'visit_date': None
                
        }
    })