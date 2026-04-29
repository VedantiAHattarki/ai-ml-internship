import os
import fitz  # PyMuPDF

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]
VIDEO_EXTENSIONS = [".mp4", ".avi", ".mov", ".mkv", ".wmv"]
PDF_EXTENSIONS = [".pdf"]


def is_digital_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        extracted_text = ""

        for page in doc:
            extracted_text += page.get_text()

        doc.close()

        return len(extracted_text.strip()) > 50

    except Exception:
        return False


def classify_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension in PDF_EXTENSIONS:
        if is_digital_pdf(file_path):
            return "digital_pdf"
        else:
            return "image_pdf"

    elif extension in IMAGE_EXTENSIONS:
        return "image"

    elif extension in VIDEO_EXTENSIONS:
        return "video"

    else:
        return "unknown"