from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "AI/ML OCR FastAPI API is running"
    assert response.json()["swagger_ui"] == "/docs"
    