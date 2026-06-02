import boto3
from app.core.config import REGION

def get_s3_client():
    return boto3.client(
        "s3",
        region_name=REGION
    )