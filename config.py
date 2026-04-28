import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REGION = "ap-south-1"

INPUT_BUCKET = "ai-ml-project-bucket"
OUTPUT_BUCKET = "ai-ml-project-bucket"

INPUT_PREFIX = "input/"
OUTPUT_PREFIX = "output/"