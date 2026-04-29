import os

REGION = "ap-south-1"

INPUT_BUCKET = "ai-ml-project-bucket"
OUTPUT_BUCKET = "ai-ml-project-bucket"

INPUT_PREFIX = "input/"
OUTPUT_PREFIX = "output/"
PROCESSED_PREFIX = "processed/"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")