import os
from dotenv import load_dotenv

DOWNLOAD_DIR_NAME = "download"

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DOTENV_FILE_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(DOTENV_FILE_PATH)

# アクセスキーの取得
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")

AWS_S3_BUCKET_NAME = os.environ.get("AWS_S3_BUCKET_NAME")
