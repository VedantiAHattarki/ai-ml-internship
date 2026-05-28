from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.file_utils import save_uploaded_file
from app.services.image_service import extract_text_from_image

router = APIRouter()


@router.post(
    "/process",
    summary="Extract text from image",
    description="Upload an image file such as JPG, JPEG, or PNG and extract text using OCR."
)
async def process_image(file: UploadFile = File(...)):
    try:
        allowed_extensions = [".jpg", ".jpeg", ".png"]

        if not any(file.filename.lower().endswith(ext) for ext in allowed_extensions):
            raise HTTPException(
                status_code=400,
                detail="Invalid image file. Please upload JPG, JPEG, or PNG file."
            )

        file_path = save_uploaded_file(file)
        extracted_text = extract_text_from_image(file_path)

        return {
            "status": "success",
            "filename": file.filename,
            "file_type": "image",
            "extracted_text": extracted_text
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error while processing image: {str(e)}"
        )