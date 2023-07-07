from dotenv import load_dotenv
import os
import requests

load_dotenv()

def detect_plate(image_file):
    url = os.getenv('API_PLATE_IDENTIFIER_ADDRESS')

    headers = {'accept': 'application/json'}
    files = {'img_file': open(image_file, 'rb')}

    response = requests.post(url, headers=headers, files=files)

    return response

