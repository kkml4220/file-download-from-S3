import os

from botocore.exceptions import ClientError

from downloader.logger import logger
from downloader.s3client import s3_client
from downloader.settings import AWS_S3_BUCKET_NAME, BASE_DIR, DOWNLOAD_DIR_NAME


def get_basename(filepath):
    """ファイルパスからbasenameを取得"""
    return os.path.basename(filepath)


def get_download_dir_path():
    """ダウンロードディレクトリのパスを取得"""
    download_dir_path = os.path.join(BASE_DIR, DOWNLOAD_DIR_NAME)
    if not os.path.exists(download_dir_path):
        os.makedirs(download_dir_path)
    assert os.path.exists(download_dir_path)

    return download_dir_path


def get_bucket_object_list(bucket_name=AWS_S3_BUCKET_NAME, prefix=""):
    """S3バケットからオブジェクトリストを取得

    Returns:
        list: オブジェクトのリスト
    """
    objects = []

    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix
        )
        logger.debug(response)
    except ClientError as e:
        logger.error(e)
        return

    for content in response["Contents"]:
        logger.debug(content)
        objects.append(content["Key"])

    return objects


def download_all_files_from_s3(bucket_name=AWS_S3_BUCKET_NAME):
    """S3内にあるすべてのオブジェクトをローカルにダウンロード"""
    download_dir_path = get_download_dir_path()
    objects = get_bucket_object_list(bucket_name=bucket_name)

    for object in objects:
        object_basename = get_basename(object)
        destination_path = os.path.join(download_dir_path, object_basename)
        try:
            s3_client.download_file(bucket_name, object, destination_path)
            logger.debug(f"download {object_basename} to {destination_path}")
        except ClientError as e:
            logger.error(e)
