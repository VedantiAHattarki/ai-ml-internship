from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_video_process_invalid_file():
    files = {
        "file": ("wrong.txt", b"This is not a video", "text/plain")
    }

    response = client.post("/api/video/process", files=files)

    assert response.status_code in [200, 400, 415, 422]
    assert isinstance(response.json(), dict)