from io import BytesIO
from fastapi import UploadFile
from app.utils.file_utils import save_uploaded_file


def test_save_uploaded_file():
    file_content = b"Sample file content"

    upload_file = UploadFile(
        filename="test_sample.txt",
        file=BytesIO(file_content)
    )

    saved_path = save_uploaded_file(upload_file)

    assert saved_path.endswith("test_sample.txt")

    with open(saved_path, "rb") as file:
        assert file.read() == file_content