import os
import fitz  # PyMuPDF
import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

POPPLER_PATH = r"C:\Users\hatta\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"


def clean_text(text):
    return text.replace("\x0c", "").replace("-\n", "").strip()


def preprocess_image(pil_image):
    image = np.array(pil_image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    gray = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2
    )

    return thresh


def extract_text_from_digital_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text()
        page_text = clean_text(page_text)

        if page_text:
            text += f"\n--- Page {page_num} ---\n{page_text}\n"

    doc.close()
    return text.strip()


def extract_text_from_scanned_pdf(pdf_path):
    images = convert_from_path(
        pdf_path,
        dpi=300,
        poppler_path=POPPLER_PATH
    )

    full_text = ""

    for i, img in enumerate(images, start=1):
        print(f"Processing scanned page {i}...")

        processed_image = preprocess_image(img)

        config = r"--oem 3 --psm 6"
        text = pytesseract.image_to_string(processed_image, config=config)
        text = clean_text(text)

        if text:
            full_text += f"\n--- Page {i} ---\n{text}\n"

    return full_text.strip()


def extract_text_from_pdf(pdf_path):
    try:
        if not os.path.exists(pdf_path):
            return "Error: PDF file not found"

        if os.path.getsize(pdf_path) == 0:
            return "Error: Uploaded PDF file is empty"

        with open(pdf_path, "rb") as file:
            header = file.read(1024)

        if b"%PDF" not in header:
            return "Error: Uploaded file is not a valid PDF"

        digital_text = extract_text_from_digital_pdf(pdf_path)

        if len(digital_text.strip()) > 50:
            return digital_text

        print("Digital text not found. Applying OCR...")
        scanned_text = extract_text_from_scanned_pdf(pdf_path)

        if scanned_text:
            return scanned_text

        return "No readable text found in PDF"

    except Exception as e:
        return f"Error while processing PDF: {str(e)}"


if __name__ == "__main__":
    input_pdf = "pdf_to_text.pdf"
    output_file = "sample_output.txt"

    result = extract_text_from_pdf(input_pdf)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result)

    print(f"Done! Text saved in {output_file}")