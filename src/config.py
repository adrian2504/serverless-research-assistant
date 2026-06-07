import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    aws_region: str
    s3_bucket: str
    bedrock_model_id: str


def get_settings() -> Settings:
    aws_region = os.getenv("AWS_REGION", "us-east-1")
    s3_bucket = os.getenv("S3_BUCKET")
    bedrock_model_id = os.getenv("BEDROCK_MODEL_ID")

    missing = []
    if not s3_bucket:
        missing.append("S3_BUCKET")
    if not bedrock_model_id:
        missing.append("BEDROCK_MODEL_ID")

    if missing:
        raise ValueError(f"Missing environment variables: {', '.join(missing)}")

    return Settings(
        aws_region=aws_region,
        s3_bucket=s3_bucket,
        bedrock_model_id=bedrock_model_id,
    )