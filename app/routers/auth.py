from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/ping")
def ping():
    return {"message": "Auth router is working"}
