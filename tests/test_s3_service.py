from unittest.mock import patch, MagicMock
from app.services import s3_service


@patch("app.services.s3_service.boto3.client")
def test_get_s3_client(mock_boto_client):
    mock_client = MagicMock()
    mock_boto_client.return_value = mock_client

    result = s3_service.get_s3_client()

    assert result == mock_client
    mock_boto_client.assert_called_once()


@patch("app.services.s3_service.get_s3_client")
def test_download_file_from_s3(mock_get_s3_client, tmp_path):
    mock_s3 = MagicMock()
    mock_get_s3_client.return_value = mock_s3

    local_file_path = tmp_path / "downloads" / "sample.pdf"

    result = s3_service.download_file_from_s3(
        s3_key="input/sample.pdf",
        local_path=str(local_file_path)
    )

    mock_s3.download_file.assert_called_once_with(
        s3_service.INPUT_BUCKET,
        "input/sample.pdf",
        str(local_file_path)
    )

    assert result == str(local_file_path)


@patch("app.services.s3_service.get_s3_client")
def test_upload_file_to_s3(mock_get_s3_client, tmp_path):
    mock_s3 = MagicMock()
    mock_get_s3_client.return_value = mock_s3

    local_file = tmp_path / "sample_output.txt"
    local_file.write_text("OCR output text")

    result = s3_service.upload_file_to_s3(
        local_path=str(local_file),
        s3_key="output/sample_output.txt"
    )

    mock_s3.upload_file.assert_called_once_with(
        str(local_file),
        s3_service.OUTPUT_BUCKET,
        "output/sample_output.txt"
    )

    assert result == "output/sample_output.txt"