from fastapi import APIRouter

router = APIRouter(
    prefix="/recruitment",
    tags=["Recruitment"]
)

@router.get("/ping")
def ping():
    return {"message": "Recruitment router is working"}
