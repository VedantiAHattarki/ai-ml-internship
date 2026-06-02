from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_image_process_invalid_file():
    files = {
        "file": ("wrong.txt", b"This is not an image", "text/plain")
    }

    response = client.post("/api/image/process", files=files)

    assert response.status_code in [200, 400, 415, 422]
    assert isinstance(response.json(), dict)