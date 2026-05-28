import os
import time
from datetime import datetime

from app.core.config import (
    INPUT_BUCKET,
    INPUT_PREFIX,
    OUTPUT_PREFIX,
    PROCESSED_PREFIX
)

from app.services.s3_service import (
    get_s3_client,
    download_file_from_s3,
    upload_file_to_s3
)



from app.services.classifier_service import classify_file
from app.services.pdf_service import extract_text_from_pdf
from app.services.image_service import extract_text_from_image
from app.services.video_service import extract_text_from_video


TEMP_FOLDER = "temp"

os.makedirs(TEMP_FOLDER, exist_ok=True)


def list_input_files():
    """
    List all files available in the S3 input folder.
    """
    s3 = get_s3_client()

    response = s3.list_objects_v2(
        Bucket=INPUT_BUCKET,
        Prefix=INPUT_PREFIX
    )

    files = []

    if "Contents" in response:
        for obj in response["Contents"]:
            key = obj["Key"]

            if key.endswith("/"):
                continue

            files.append(key)

    return files


def process_file(local_file_path: str, file_type: str) -> str:
    """
    Route the downloaded file to the correct OCR service.
    """
    if file_type in ["pdf", "digital_pdf", "image_pdf"]:
        return extract_text_from_pdf(local_file_path)

    if file_type == "image":
        return extract_text_from_image(local_file_path)

    if file_type == "video":
        return extract_text_from_video(local_file_path)

    return f"Unsupported file type: {file_type}"


def move_file_to_processed(s3_key: str) -> str:
    """
    Move processed file from input folder to processed folder in S3.
    """
    s3 = get_s3_client()

    file_name = os.path.basename(s3_key)
    processed_key = PROCESSED_PREFIX + file_name

    s3.copy_object(
        Bucket=INPUT_BUCKET,
        CopySource={
            "Bucket": INPUT_BUCKET,
            "Key": s3_key
        },
        Key=processed_key
    )

    s3.delete_object(
        Bucket=INPUT_BUCKET,
        Key=s3_key
    )

    return processed_key


def handle_s3_file(s3_key: str):
    """
    Download, classify, process, upload output, and move original file.
    """
    print(f"\nNew file found: {s3_key}")

    file_name = os.path.basename(s3_key)
    local_file_path = os.path.join(TEMP_FOLDER, file_name)

    download_file_from_s3(s3_key, local_file_path)

    file_type = classify_file(local_file_path)
    print(f"Detected file type: {file_type}")

    extracted_text = process_file(local_file_path, file_type)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_name = f"{os.path.splitext(file_name)[0]}_{timestamp}.txt"
    local_output_path = os.path.join(TEMP_FOLDER, output_file_name)

    with open(local_output_path, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    output_s3_key = OUTPUT_PREFIX + output_file_name
    upload_file_to_s3(local_output_path, output_s3_key)

    processed_key = move_file_to_processed(s3_key)

    print(f"Output uploaded to: {output_s3_key}")
    print(f"Input moved to processed folder: {processed_key}")


def monitor_s3_folder():
    """
    Continuously monitor the S3 input folder every 60 seconds.
    """
    print("Scheduler started...")
    print(f"Monitoring S3 folder: s3://{INPUT_BUCKET}/{INPUT_PREFIX}")

    while True:
        try:
            files = list_input_files()

            if files:
                for s3_key in files:
                    handle_s3_file(s3_key)
            else:
                print("No new files found.")

        except Exception as e:
            print(f"Scheduler error: {str(e)}")

        time.sleep(60)


if __name__ == "__main__":
    monitor_s3_folder()