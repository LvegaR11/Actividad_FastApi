from pydantic import BaseModel, EmailStr,ConfigDict


class UserRequestModel(BaseModel):
    name: str
    password: str
    last_name: str
    role: str
    email: EmailStr
    phone: str
    status: str
   
    @classmethod
    def validate_name(cls, name: str) -> str:
       if len(name) < 3:
           raise ValueError('Name must be at least 3 characters long')
       if len(name) > 50:
           raise ValueError('Name must be at most 50 characters long')
       return name
    model_config = ConfigDict(json_schema_extra={
        'example': {
            'name': 'luis',
            'password': '1234',
            'last_name': 'vega',
            'role': 'admin',
            'email': 'Luis@example.com',
            'phone': '3007056108',
            'status': 'active'
        }
    })

class UserResponseModel(BaseModel):
    id: int 
    name: str
    last_name: str
    role: str
    email: EmailStr
    phone: str
    status: str
    created_at: str
    model_config = ConfigDict(from_attributes=True)