

import os
from dotenv import load_dotenv

load_dotenv()

# AWS region
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

# S3 bucket names
INPUT_BUCKET = os.getenv("INPUT_BUCKET", "ai-ml-project-bucket")
OUTPUT_BUCKET = os.getenv("OUTPUT_BUCKET", "ai-ml-project-bucket")

# S3 folder prefixes
INPUT_PREFIX = os.getenv("INPUT_PREFIX", "input/")
OUTPUT_PREFIX = os.getenv("OUTPUT_PREFIX", "output/")
PROCESSED_PREFIX = os.getenv("PROCESSED_PREFIX", "processed/")

# AWS credentials
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Local temporary folder
TEMP_FOLDER = os.getenv("TEMP_FOLDER", "temp")