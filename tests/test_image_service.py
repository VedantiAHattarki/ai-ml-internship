from unittest.mock import patch
from app.services import image_service


def test_clean_text_image_service():
    result = image_service.clean_text(" Hello OCR \x0c ")
    assert result == "Hello OCR"


@patch("app.services.image_service.os.path.exists")
def test_extract_text_from_image_file_not_found(mock_exists):
    mock_exists.return_value = False

    result = image_service.extract_text_from_image("missing.png")

    assert result == "Error: Image file not found"


@patch("app.services.image_service.os.path.exists")
@patch("app.services.image_service.preprocess_image")
def test_extract_text_from_image_unreadable(mock_preprocess, mock_exists):
    mock_exists.return_value = True
    mock_preprocess.return_value = None

    result = image_service.extract_text_from_image("sample.png")

    assert result == "Error: Unable to read image file"


@patch("app.services.image_service.os.path.exists")
@patch("app.services.image_service.preprocess_image")
@patch("app.services.image_service.pytesseract.image_to_string")
def test_extract_text_from_image_success(mock_ocr, mock_preprocess, mock_exists):
    mock_exists.return_value = True
    mock_preprocess.return_value = "processed_image"
    mock_ocr.return_value = " OCR extracted text \x0c "

    result = image_service.extract_text_from_image("sample.png")

    assert result == "OCR extracted text"


@patch("app.services.image_service.os.path.exists")
@patch("app.services.image_service.preprocess_image")
@patch("app.services.image_service.pytesseract.image_to_string")
def test_extract_text_from_image_no_text(mock_ocr, mock_preprocess, mock_exists):
    mock_exists.return_value = True
    mock_preprocess.return_value = "processed_image"
    mock_ocr.return_value = " \x0c "

    result = image_service.extract_text_from_image("sample.png")

    assert result == "No readable text found in image"


@patch("app.services.image_service.os.path.exists")
@patch("app.services.image_service.preprocess_image")
def test_extract_text_from_image_exception(mock_preprocess, mock_exists):
    mock_exists.return_value = True
    mock_preprocess.side_effect = Exception("test error")

    result = image_service.extract_text_from_image("sample.png")

    assert "Error while processing image" in result