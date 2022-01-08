
import requests
from typing import *

BASE_URL = 'http://127.0.0.1:5000'
class ROUTES:
    TRANSFORM = '/transform'
    LOGIN = '/login'

def transformImage(image) -> Dict:
    headers = {}
    payload = {}
    files = [
        ('image', (image.name, open('./05000.png', 'rb'), 'image/png'))
    ]
    response = requests.request("POST", f'{BASE_URL}{ROUTES.TRANSFORM}', headers=headers, data=payload, files=files)

    video = {
        'bytes': response.content,
        'format': response.headers['Content-Type']
    }
    
    print(video['format'])
    return video
