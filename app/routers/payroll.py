from fastapi import APIRouter

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)

@router.get("/ping")
def ping():
    return {"message": "Payroll router is working"}
