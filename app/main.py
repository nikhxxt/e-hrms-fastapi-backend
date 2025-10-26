from fastapi import FastAPI
from app.routers import employees, auth, attendance, payroll, appraisal, recruitment

app = FastAPI(title="E-HRMS API")

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(attendance.router)
app.include_router(payroll.router)
app.include_router(appraisal.router)
app.include_router(recruitment.router)
