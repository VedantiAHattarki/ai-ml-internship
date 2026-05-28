import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "temp"


def save_uploaded_file(request):
    """
    Saves uploaded file from Flask request into temp folder.
    Returns saved file path.
    """

    if "file" not in request.files:
        return None, "No file found in request"

    file = request.files["file"]

    if file.filename == "":
        return None, "No file selected"

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(file_path)

    return file_path, None