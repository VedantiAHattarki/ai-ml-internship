from unittest.mock import patch, MagicMock, mock_open
from app.services import pdf_service


def test_clean_text_pdf_service():
    result = pdf_service.clean_text("Hello-\nWorld\x0c ")
    assert result == "HelloWorld"


@patch("app.services.pdf_service.os.path.exists")
def test_extract_text_from_pdf_file_not_found(mock_exists):
    mock_exists.return_value = False

    result = pdf_service.extract_text_from_pdf("missing.pdf")

    assert result == "Error: PDF file not found"


@patch("app.services.pdf_service.os.path.exists")
@patch("app.services.pdf_service.os.path.getsize")
def test_extract_text_from_pdf_empty_file(mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = 0

    result = pdf_service.extract_text_from_pdf("empty.pdf")

    assert result == "Error: Uploaded PDF file is empty"


@patch("app.services.pdf_service.os.path.exists")
@patch("app.services.pdf_service.os.path.getsize")
@patch("builtins.open", new_callable=mock_open, read_data=b"NOT A PDF FILE")
def test_extract_text_from_pdf_invalid_file(mock_file, mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = 100

    result = pdf_service.extract_text_from_pdf("invalid.pdf")

    assert result == "Error: Uploaded file is not a valid PDF"


@patch("app.services.pdf_service.os.path.exists")
@patch("app.services.pdf_service.os.path.getsize")
@patch("builtins.open", new_callable=mock_open, read_data=b"%PDF sample")
@patch("app.services.pdf_service.extract_text_from_digital_pdf")
def test_extract_text_from_pdf_digital_success(
    mock_digital,
    mock_file,
    mock_getsize,
    mock_exists
):
    mock_exists.return_value = True
    mock_getsize.return_value = 100
    mock_digital.return_value = "This is digital PDF text with more than fifty characters for testing coverage."

    result = pdf_service.extract_text_from_pdf("sample.pdf")

    assert "digital PDF text" in result


@patch("app.services.pdf_service.os.path.exists")
@patch("app.services.pdf_service.os.path.getsize")
@patch("builtins.open", new_callable=mock_open, read_data=b"%PDF sample")
@patch("app.services.pdf_service.extract_text_from_digital_pdf")
@patch("app.services.pdf_service.extract_text_from_scanned_pdf")
def test_extract_text_from_pdf_scanned_success(
    mock_scanned,
    mock_digital,
    mock_file,
    mock_getsize,
    mock_exists
):
    mock_exists.return_value = True
    mock_getsize.return_value = 100
    mock_digital.return_value = "short"
    mock_scanned.return_value = "Scanned PDF OCR text"

    result = pdf_service.extract_text_from_pdf("sample.pdf")

    assert result == "Scanned PDF OCR text"


@patch("app.services.pdf_service.os.path.exists")
@patch("app.services.pdf_service.os.path.getsize")
@patch("builtins.open", new_callable=mock_open, read_data=b"%PDF sample")
@patch("app.services.pdf_service.extract_text_from_digital_pdf")
@patch("app.services.pdf_service.extract_text_from_scanned_pdf")
def test_extract_text_from_pdf_no_text(
    mock_scanned,
    mock_digital,
    mock_file,
    mock_getsize,
    mock_exists
):
    mock_exists.return_value = True
    mock_getsize.return_value = 100
    mock_digital.return_value = "short"
    mock_scanned.return_value = ""

    result = pdf_service.extract_text_from_pdf("sample.pdf")

    assert result == "No readable text found in PDF"


@patch("app.services.pdf_service.fitz.open")
def test_extract_text_from_digital_pdf(mock_fitz_open):
    mock_page = MagicMock()
    mock_page.get_text.return_value = "Sample digital page text"

    mock_doc = MagicMock()
    mock_doc.__iter__.return_value = [mock_page]
    mock_fitz_open.return_value = mock_doc

    result = pdf_service.extract_text_from_digital_pdf("sample.pdf")

    assert "Sample digital page text" in result
    mock_doc.close.assert_called_once()


@patch("app.services.pdf_service.convert_from_path")
@patch("app.services.pdf_service.preprocess_pdf_page")
@patch("app.services.pdf_service.pytesseract.image_to_string")
def test_extract_text_from_scanned_pdf(mock_ocr, mock_preprocess, mock_convert):
    mock_convert.return_value = ["page_image"]
    mock_preprocess.return_value = "processed_page"
    mock_ocr.return_value = "Scanned page text"

    result = pdf_service.extract_text_from_scanned_pdf("sample.pdf")

    assert "Scanned page text" in result