# file-download-from-S3

AWS S3 からバケット内のすべてのファイルをダウンロード

## Installation

最初に必要なパッケージをインストールしてください

```bash
pip install -r requirements.txt
```

## Usage

### 環境変数の設定

`setup.py`を実行して必要な環境変数を入力してください。実際には`*`部分は入力した文字になります。

```bash
> python setup.py
AWS_ACCESS_KEY_IDを入力してください：************
AWS_SECRET_ACCESS_KEYを入力してください：*********
AWS_S3_BUCKET_NAMEを入力してください：************
AWS_DEFAULT_REGIONを入力してください：************
```

ディレクトリに`.env`ファイルが生成されていることを確認してください

```plaintext
AWS_ACCESS_KEY_ID="************"
AWS_SECRET_ACCESS_KEY="*********"
AWS_S3_BUCKET_NAME="************"
AWS_DEFAULT_REGION="************"
```

### 実行方法

```bash
> python main.py
```
