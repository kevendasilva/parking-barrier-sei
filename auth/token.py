from requests.exceptions import RequestException

from auth.login import login
from request.get import get
from setup import root_dir
from utils.files import read_file
from utils.variables import get_variable

def get_token(credentials_file_path):
    filename = 'token'
    token = read_file(filename, root_dir)
    valid_token = check_token(token)

    if valid_token:
        return valid_token

    new_token = login(credentials_file_path)

    if new_token:
        return new_token

    return None


def check_token(token):
    api_url = get_variable('API_URL')
    if not api_url:
        return None

    headers = { 'Authorization': token }

    try:
        response = get(api_url, '/current_administrator', headers=headers)

        if response.status_code == 200:
            return token

        if response.status_code == 401:
            return False

        print("Error verifying token:", response.text)
        return None

    except RequestException as e:
        print("API connection error:", str(e))
        return None
