from dotenv import load_dotenv
import os

def load_env_variables(file_path=".env"):
    """
    Load environment variables from a .env file.

    Parameters:
    - file_path (str): The path to the .env file. Default is ".env" in the current directory.

    Returns:
    - dict: A dictionary containing the loaded environment variables.
    """
    load_dotenv(file_path)

    env_variables = {}
    with open(file_path, "r") as file:
        for line in file:
            # Skip comments and empty lines
            if line.strip() and not line.strip().startswith("#"):
                key, value = line.strip().split("=", 1)
                env_variables[key] = value

    return env_variables

if __name__=='__main__':
    
    # .env 파일 내의 환경 변수 읽어오기
    env_variables = load_env_variables()

    # 결과 출력
    for key, value in env_variables.items():
        print(f"{key}: {value}")


