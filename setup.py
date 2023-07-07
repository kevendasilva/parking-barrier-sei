# Setup of the project

from dotenv import load_dotenv
import os

from utils.variables import get_variable
from utils.files import file_exists

load_dotenv()

root_dir = os.path.dirname(os.path.abspath(__file__))

credentials_file = {
    "name": "credentials.json",
    "path": root_dir
}
credentials_file_path = f"{root_dir}/{credentials_file['name']}"

dotenv_file =  {
    "name": ".env",
    "path": root_dir
}

def load_configs():
    files = [credentials_file, dotenv_file]

    if not all_necessary_files_exist(files):
        return False

    api_url = get_variable('API_URL')

    if not api_url:
        return False


def all_necessary_files_exist(files):
    for file in files:
        if not file_exists(file["name"], file["path"]):
            return False

    return True

