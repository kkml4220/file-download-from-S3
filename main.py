from downloader.download import download_all_files_from_s3
from downloader.logger import logger

from downloader.settings import (
    AWS_S3_BUCKET_NAME
)


def main():
    logger.info(f"開始：{AWS_S3_BUCKET_NAME}からファイルをダウンロード")
    download_all_files_from_s3()
    logger.info(f"終了：{AWS_S3_BUCKET_NAME}からファイルをダウンロード")


if __name__ == '__main__':
    main()
