from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "FastAPI OCR project is running successfully"
    }