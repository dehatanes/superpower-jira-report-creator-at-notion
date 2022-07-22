import logging
import boto3
from botocore.exceptions import ClientError
import os

BUCKET_NAME = os.environ.get("BUCKET_NAME")


def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(file_name, BUCKET_NAME, object_name)
        return f"https://{BUCKET_NAME}.s3.amazonaws.com/{object_name}"
    except ClientError as e:
        logging.error(e)


if __name__ == '__main__':
    # Just used to test requests in dev env
    print(upload_file("temp_dashboard_image.png"))
