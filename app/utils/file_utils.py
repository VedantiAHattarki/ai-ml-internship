import os
import shutil
from fastapi import UploadFile

TEMP_DIR = "temp"

os.makedirs(TEMP_DIR, exist_ok=True)


def save_uploaded_file(file: UploadFile) -> str:
    file_path = os.path.join(TEMP_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path