from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.file_utils import save_uploaded_file
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()


@router.post(
    "/process",
    summary="Extract text from PDF",
    description="Upload a PDF file and extract text from digital or scanned PDF using OCR."
)
async def process_pdf(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Invalid PDF file. Please upload a PDF file."
            )

        file_path = save_uploaded_file(file)
        extracted_text = extract_text_from_pdf(file_path)

        return {
            "status": "success",
            "filename": file.filename,
            "file_type": "pdf",
            "extracted_text": extracted_text
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error while processing PDF: {str(e)}"
        )