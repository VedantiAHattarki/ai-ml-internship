import os
import cv2
import pytesseract
from difflib import SequenceMatcher

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def clean_text(text: str) -> str:
    lines = text.replace("\x0c", "").splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if len(line) < 5:
            continue

        letters = sum(c.isalpha() for c in line)

        if letters / max(len(line), 1) < 0.5:
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def is_similar(text1: str, text2: str, threshold: float = 0.75) -> bool:
    if not text1 or not text2:
        return False

    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity >= threshold


def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.resize(
        gray,
        None,
        fx=1.5,
        fy=1.5,
        interpolation=cv2.INTER_CUBIC
    )

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


def extract_text_from_video(video_path: str) -> str:
    try:
        if not os.path.exists(video_path):
            return "Error: Video file not found"

        capture = cv2.VideoCapture(video_path)

        if not capture.isOpened():
            return "Error: Cannot open video file"

        fps = capture.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 30

        frame_interval = int(fps * 5)

        frame_count = 0
        unique_texts = []
        last_text = ""

        while True:
            ret, frame = capture.read()

            if not ret:
                break

            if frame_count % frame_interval == 0:
                processed_frame = preprocess_frame(frame)

                config = r"--oem 3 --psm 11"
                text = pytesseract.image_to_string(
                    processed_frame,
                    config=config
                )

                cleaned_text = clean_text(text)

                if cleaned_text and not is_similar(cleaned_text, last_text):
                    if cleaned_text not in unique_texts:
                        unique_texts.append(cleaned_text)
                        last_text = cleaned_text

            frame_count += 1

        capture.release()
        cv2.destroyAllWindows()

        if unique_texts:
            return "\n\n".join(unique_texts)

        return "No readable text found in video"

    except Exception as e:
        return f"Error while processing video: {str(e)}"