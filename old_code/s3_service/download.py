import os
from s3_service.s3_client import get_s3_client
from config import INPUT_BUCKET

def download_file_from_s3(s3_key, local_path):
    s3 = get_s3_client()

    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    s3.download_file(INPUT_BUCKET, s3_key, local_path)

    return local_path