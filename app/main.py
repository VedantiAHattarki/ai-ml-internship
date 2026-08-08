from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import routes_health
from app.api import routes_pdf
from app.api import routes_image
from app.api import routes_video

app = FastAPI(
    title="Case Intake Processor",
    description="""
    This project provides OCR APIs for:

    - PDF to text extraction
    - Image to text extraction
    - Video to text extraction
    - File classification
    - AWS S3 integration
    """,
    version="1.0.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "docExpansion": "none"
    }
)

# Add CORS (new)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_health.router, prefix="/api", tags=["Health Check"])
app.include_router(routes_pdf.router, prefix="/api/pdf", tags=["PDF OCR"])
app.include_router(routes_image.router, prefix="/api/image", tags=["Image OCR"])
app.include_router(routes_video.router, prefix="/api/video", tags=["Video OCR"])


@app.get("/")
def home():
    return {
        "message": "AI/ML OCR FastAPI API is running",
        "swagger_ui": "/docs",
        "endpoints": [
            "/api/health",
            "/api/pdf/process",
            "/api/image/process",
            "/api/video/process"
        ]
    }