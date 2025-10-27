from fastapi import APIRouter

router = APIRouter(
    prefix="/appraisal",
    tags=["Appraisal"]
)

@router.get("/ping")
def ping():
    return {"message": "Appraisal router is working"}
