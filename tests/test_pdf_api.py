from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_pdf_process_invalid_file():
    files = {
        "file": ("test.txt", b"This is not a PDF file", "text/plain")
    }

    response = client.post("/api/pdf/process", files=files)

    assert response.status_code in [200, 400, 415, 422]
    assert isinstance(response.json(), dict)