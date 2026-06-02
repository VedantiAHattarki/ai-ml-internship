from app.services.classifier_service import classify_file


def test_classify_pdf_file():
    result = classify_file("sample.pdf")
    assert result == "image_pdf"


def test_classify_png_image_file():
    result = classify_file("sample.png")
    assert result == "image"


def test_classify_jpg_image_file():
    result = classify_file("sample.jpg")
    assert result == "image"


def test_classify_jpeg_image_file():
    result = classify_file("sample.jpeg")
    assert result == "image"


def test_classify_video_file():
    result = classify_file("sample.mp4")
    assert result == "video"


def test_classify_unknown_file():
    result = classify_file("sample.txt")
    assert result in ["unknown", None]