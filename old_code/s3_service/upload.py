from s3_service.s3_client import get_s3_client
from config import OUTPUT_BUCKET

def upload_file_to_s3(local_path, s3_key):
    s3 = get_s3_client()

    s3.upload_file(local_path, OUTPUT_BUCKET, s3_key)

    return s3_key