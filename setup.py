import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 環境変数設定用ファイルパス
DOTENV_FILE_PATH = os.path.join(BASE_DIR, '.env')


# 確認する環境変数のリスト
env_variables = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY",
                 "AWS_S3_BUCKET_NAME", "AWS_DEFAULT_REGION"]


def get_missing_env_variables():
    """未定義の環境変数の環境変数名を取得

    Returns:
        list: 未定義の環境変数名のリスト
    """
    missing_variables = []

    for varriable in env_variables:
        if varriable not in os.environ:
            missing_variables.append(varriable)

    return missing_variables


def get_variable_from_prompt(variable):
    """環境変数をプロンプトから入力
    Args:
        variable (str): 環境変数名
    Returns:
        str: 入力された環境変数の値
    """
    value = input(f"{variable}を入力してください：")
    return value


def write_to_env_file(variable, value):
    """envファイルに環境変数を書き込む
    Args:
        variable (str): 環境変数名
        value (str): 環境変数の値
    """
    with open(DOTENV_FILE_PATH, 'a') as env_file:
        env_file.write(f'{variable}="{value}"\n')


def setup_env_variables():
    missing_variables = get_missing_env_variables()

    if not missing_variables:
        print("すべての環境変数が定義済みです")
        return

    for variable in missing_variables:
        value = get_variable_from_prompt(variable)
        write_to_env_file(variable, value)


if __name__ == "__main__":
    setup_env_variables()
