import os
import boto3

from app.core.config import (
    AWS_REGION,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    INPUT_BUCKET,
    OUTPUT_BUCKET
)


def get_s3_client():
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        return boto3.client(
            "s3",
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

    return boto3.client(
        "s3",
        region_name=AWS_REGION
    )


def download_file_from_s3(s3_key: str, local_path: str) -> str:
    s3 = get_s3_client()

    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    s3.download_file(INPUT_BUCKET, s3_key, local_path)

    return local_path


def upload_file_to_s3(local_path: str, s3_key: str) -> str:
    s3 = get_s3_client()

    s3.upload_file(local_path, OUTPUT_BUCKET, s3_key)

    return s3_key