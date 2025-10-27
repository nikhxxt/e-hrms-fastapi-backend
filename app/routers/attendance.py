from fastapi import APIRouter

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.get("/ping")
def ping():
    return {"message": "Attendance router is working"}
