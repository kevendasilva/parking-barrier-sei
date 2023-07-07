import json

from request.post import post
from utils.variables import get_variable

def login(credentials_file_path):
    api_url = get_variable('API_URL')
    if not api_url:
        return None

    with open(credentials_file_path) as f:
        client_info = json.load(f)

    response = post(api_url, '/login', client_info)

    if response.status_code == 200:
        token = response.headers.get('Authorization')

        with open('token', 'w') as f:
            f.write(token)

        return token

    print("Error logging in:", response.text)
    return None
