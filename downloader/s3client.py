import boto3

from botocore.exceptions import ClientError

from downloader.logger import logger

from downloader.settings import (
    AWS_ACCESS_KEY_ID,
    AWS_DEFAULT_REGION,
    AWS_SECRET_ACCESS_KEY)


try:
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_DEFAULT_REGION)
    logger.debug('S3 client initialized')
except ClientError as e:
    logger.error(e)
