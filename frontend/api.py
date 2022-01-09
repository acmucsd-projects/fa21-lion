
import requests
import json
from typing import *

from requests.api import request
from constants import DEBUG
#
# Constants
#

class ROUTES:
    TRANSFORM = '/transform'
    LOGIN = '/login'
    GET_VIDEO_NAMES = '/videos'
    REGISTER = '/register'
    SAVE = '/videos'
class URL:
    _BASE_URL = 'http://127.0.0.1:5000'
    @classmethod
    def getURL(cls, suffix):
        return cls._BASE_URL + suffix
#
# Data models
#
class Video:
    def __init__(self, bytes, format):
        self._bytes = bytes
        self.format = format
    
    @classmethod
    def from_response(cls, response):
        return cls(
            bytes=response.content,
            format=response.headers['Content-Type']
        )
    
    def read(self):
        return self._bytes
class UserAuth:
    def __init__(self, username, access_token) -> None:
        self.access_token = access_token
        self.username = username
    
    def get_auth_header(self):
        return f'Bearer {self.access_token}'

#    
# API Wrappers
#

def transformImage(image) -> Tuple[bool, Video]:
    if (DEBUG): print('DEBUG: transformImage called')
    response = requests.request(
        method="POST", 
        url=URL.getURL(ROUTES.TRANSFORM), 
        headers={}, 
        data={}, 
        files=[
            ('image', (image.name, image.read(), image.type))
        ]
    )

    if (response.status_code != 200):
        return False, None
    
    return True, Video.from_response(response)

def get_file(auth: UserAuth, filename) -> Tuple[bool, Video]:
    if (DEBUG): print('DEBUG: get_file called')
    response = requests.request(
        method='GET',
        url=URL.getURL(ROUTES.GET_VIDEO_NAMES) + f'/{filename}',
        headers={
            'Authorization': auth.get_auth_header()
        },
        data={}
    )
    if response.status_code != 200:
        return False, None
    
    return True, Video.from_response(response)

def register(username, password) -> bool:
    response = requests.request(
        method='POST',
        url=URL.getURL(ROUTES.REGISTER),
        headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            'username': username,
            'password': password
        }),
    )
    return response.status_code == 200

def login(username, password) -> Tuple[bool, UserAuth]:
    if (DEBUG): print(f'DEBUG: username {username} password {password}')

    response = requests.request(
        "POST",
        URL.getURL(ROUTES.LOGIN),
        headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            'username': username,
            'password': password,
        })
    )

    response_json = json.loads(response.text)
    if response.status_code != 200:
        return False, None
    
    access_token = response_json.get('tokens').get('access_token')
    return True, UserAuth(username, access_token)

def save_transformation(auth: UserAuth, video: Video) -> Tuple[bool, str]:
    if (DEBUG): print('DEBUG: save_transformation called')
    response = requests.request(
        'POST',
        URL.getURL(ROUTES.SAVE),
        headers={
            'Authorization': auth.get_auth_header(),
        },
        data={},
        files=[
            ('video', ('video.mp4', video.read(), video.format))
        ]
    )
    if response.status_code != 200:
        error_message = 'Some server error occured.'
        if (response.headers['Content-Type'] == 'application/json'):
            error_message = json.loads(response.text).get('msg')
        return False, error_message
    
    return True, None

def get_video_names(auth: UserAuth) -> Tuple[bool, Union[str, List[str]]]:
    if (DEBUG): print(f'DEBUG: get_video_names called')
    response = requests.request(
        "GET",
        URL.getURL(ROUTES.GET_VIDEO_NAMES),
        headers={
            'Authorization': auth.get_auth_header()
        },
        data={}
    )

    response_json = json.loads(response.text)
    if response.status_code != 200:
        print(f'ERROR: status {response.status_code} message {response_json.get("msg")}')
        return False, response_json.get('msg')
    
    video_names = response_json.get('data')
    return True, video_names