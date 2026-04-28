import time
from s3_service.s3_client import get_s3_client
from config import INPUT_BUCKET, INPUT_PREFIX
from classifier import classify_file
from s3_service.download import download_file
from s3_service.upload import upload_file

def process_file(file_path, file_type):
    if file_type == "pdf":
        from digitalpdf_to_text.pdf_to_text import extract_text_from_pdf
        return extract_text_from_pdf(file_path)

    elif file_type == "image":
        from image_to_text.image_to_text import extract_text_from_image
        return extract_text_from_image(file_path)

    elif file_type == "video":
        from video_to_text.video_to_text import extract_text_from_video
        return extract_text_from_video(file_path)

    return "Unsupported file"

def monitor_s3():
    s3 = get_s3_client()

    while True:
        response = s3.list_objects_v2(Bucket=INPUT_BUCKET, Prefix=INPUT_PREFIX)

        if "Contents" in response:
            for obj in response["Contents"]:
                key = obj["Key"]

                local_file = f"temp/{key.split('/')[-1]}"
                download_file(key, local_file)

                file_type = classify_file(local_file)
                output_text = process_file(local_file, file_type)

                output_file = local_file + ".txt"
                with open(output_file, "w") as f:
                    f.write(output_text)

                upload_file(output_file, "output/" + output_file.split("/")[-1])

        time.sleep(60)

if __name__ == "__main__":
    monitor_s3()