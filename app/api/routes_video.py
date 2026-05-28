from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.file_utils import save_uploaded_file
from app.services.video_service import extract_text_from_video

router = APIRouter()


@router.post(
    "/process",
    summary="Extract text from video",
    description="Upload a video file such as MP4, AVI, MOV, or MKV and extract visible text from video frames using OCR."
)
async def process_video(file: UploadFile = File(...)):
    try:
        allowed_extensions = [".mp4", ".avi", ".mov", ".mkv"]

        if not any(file.filename.lower().endswith(ext) for ext in allowed_extensions):
            raise HTTPException(
                status_code=400,
                detail="Invalid video file. Please upload MP4, AVI, MOV, or MKV file."
            )

        file_path = save_uploaded_file(file)
        extracted_text = extract_text_from_video(file_path)

        return {
            "status": "success",
            "filename": file.filename,
            "file_type": "video",
            "extracted_text": extracted_text
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error while processing video: {str(e)}"
        )