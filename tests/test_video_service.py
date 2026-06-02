from unittest.mock import patch, MagicMock
from app.services import video_service


def test_clean_text_video_service():
    text = "Hi\nThis is valid text\n12345\nOCR line"
    result = video_service.clean_text(text)

    assert "This is valid text" in result
    assert "Hi" not in result


def test_is_similar_empty_text():
    assert video_service.is_similar("", "hello") is False
    assert video_service.is_similar("hello", "") is False


def test_is_similar_true():
    assert video_service.is_similar("Hello OCR text", "Hello OCR text") is True


def test_is_similar_false():
    assert video_service.is_similar("Hello OCR text", "Completely different") is False


@patch("app.services.video_service.os.path.exists")
def test_extract_text_from_video_file_not_found(mock_exists):
    mock_exists.return_value = False

    result = video_service.extract_text_from_video("missing.mp4")

    assert result == "Error: Video file not found"


@patch("app.services.video_service.os.path.exists")
@patch("app.services.video_service.cv2.VideoCapture")
def test_extract_text_from_video_cannot_open(mock_video_capture, mock_exists):
    mock_exists.return_value = True

    mock_capture = MagicMock()
    mock_capture.isOpened.return_value = False
    mock_video_capture.return_value = mock_capture

    result = video_service.extract_text_from_video("sample.mp4")

    assert result == "Error: Cannot open video file"


@patch("app.services.video_service.os.path.exists")
@patch("app.services.video_service.cv2.destroyAllWindows")
@patch("app.services.video_service.cv2.VideoCapture")
@patch("app.services.video_service.preprocess_frame")
@patch("app.services.video_service.pytesseract.image_to_string")
def test_extract_text_from_video_success(
    mock_ocr,
    mock_preprocess,
    mock_video_capture,
    mock_destroy,
    mock_exists
):
    mock_exists.return_value = True

    mock_capture = MagicMock()
    mock_capture.isOpened.return_value = True
    mock_capture.get.return_value = 1
    mock_capture.read.side_effect = [
        (True, "frame1"),
        (False, None)
    ]

    mock_video_capture.return_value = mock_capture
    mock_preprocess.return_value = "processed_frame"
    mock_ocr.return_value = "This is valid video OCR text"

    result = video_service.extract_text_from_video("sample.mp4")

    assert "This is valid video OCR text" in result
    mock_capture.release.assert_called_once()


@patch("app.services.video_service.os.path.exists")
@patch("app.services.video_service.cv2.destroyAllWindows")
@patch("app.services.video_service.cv2.VideoCapture")
@patch("app.services.video_service.preprocess_frame")
@patch("app.services.video_service.pytesseract.image_to_string")
def test_extract_text_from_video_no_text(
    mock_ocr,
    mock_preprocess,
    mock_video_capture,
    mock_destroy,
    mock_exists
):
    mock_exists.return_value = True

    mock_capture = MagicMock()
    mock_capture.isOpened.return_value = True
    mock_capture.get.return_value = 1
    mock_capture.read.side_effect = [
        (True, "frame1"),
        (False, None)
    ]

    mock_video_capture.return_value = mock_capture
    mock_preprocess.return_value = "processed_frame"
    mock_ocr.return_value = "123"

    result = video_service.extract_text_from_video("sample.mp4")

    assert result == "No readable text found in video"


@patch("app.services.video_service.os.path.exists")
@patch("app.services.video_service.cv2.VideoCapture")
def test_extract_text_from_video_exception(mock_video_capture, mock_exists):
    mock_exists.return_value = True
    mock_video_capture.side_effect = Exception("video error")

    result = video_service.extract_text_from_video("sample.mp4")

    assert "Error while processing video" in result