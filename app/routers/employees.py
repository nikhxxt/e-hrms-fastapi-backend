from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, EmployeeOut
from app.models import employee
from app.db.session import get_db

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=EmployeeOut)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = employee.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp
