import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def clean_text(text):
    return text.replace("\x0c", "").strip()


def preprocess_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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


def extract_text_from_image(image_path):
    try:
        if not os.path.exists(image_path):
            return "Error: Image file not found"

        processed_image = preprocess_image(image_path)

        if processed_image is None:
            return "Error: Unable to read image file"

        config = r"--oem 3 --psm 6"
        text = pytesseract.image_to_string(processed_image, config=config)

        cleaned_text = clean_text(text)

        if cleaned_text:
            return cleaned_text

        return "No readable text found in image"

    except Exception as e:
        return f"Error while processing image: {str(e)}"


if __name__ == "__main__":
    input_image = "image_to_text.jpg"

    result = extract_text_from_image(input_image)

    print(result)