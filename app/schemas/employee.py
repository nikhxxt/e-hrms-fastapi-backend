from pydantic import BaseModel, EmailStr
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    role: str
    department: str
    date_joined: date

class EmployeeOut(EmployeeCreate):
    id: int
