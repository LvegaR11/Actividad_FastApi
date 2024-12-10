from pydantic import BaseModel, EmailStr,ConfigDict

class VisitRequestModel(BaseModel):
    location: str
    duration: float
    number_of_persons: int
    visit_date: str

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
            'visit_date': '2023-01-01'
        }
    })

    class VisitResponseModel(BaseModel):
        id: int 
        location: str
        duration: float
        number_of_persons: int
        visit_date: str
        model_config = ConfigDict(from_attributes=True)
    