import uuid
import boto3
from botocore.exceptions import ClientError
from src.config import get_settings


settings = get_settings()

s3_client = boto3.client("s3", region_name=settings.aws_region)

def create_document_key(filename: str)-> str:
    safe_filename = filename.replace(" ", "_")
    doc_id = str(uuid.uuid4())
    return f"uploads/{doc_id}_{safe_filename}"


def upload_bytes_to_s3(file_bytes: bytes, filename: str, content_type: str = "application/pdf") -> str:
    #Uploading file to S3 and returns the S3 object key.

    key = create_document_key(filename)

    try:
        s3_client.put_object(
            Bucket=settings.s3_bucket,
            Key=key,
            Body=file_bytes,
            ContentType=content_type,
        )
        return key

    except ClientError as error:
        raise RuntimeError(f"Failed to upload file to S3: {error}") from error


def save_markdown_to_s3(markdown_text: str, source_key: str) -> str:
    #Saves generated research brief as a markdown file in S3.

    output_key = source_key.replace("uploads/", "outputs/") + ".md"

    try:
        s3_client.put_object(
            Bucket=settings.s3_bucket,
            Key=output_key,
            Body=markdown_text.encode("utf-8"),
            ContentType="text/markdown", )
        return output_key
    
    except ClientError as error:
        raise RuntimeError(f"Failed to save markdown to S3: {error}") from error