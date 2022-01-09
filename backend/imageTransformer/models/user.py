import os

from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from typing import * 
import uuid

from imageTransformer.app import app, mongo
from imageTransformer.constants import USER_DOCUMENT_KEYS, ALLOWED_VIDEO_EXTENSIONS, TRANSFORMED_FILE_PREFIX
from imageTransformer.helpers import get_file_extension
from sampleTransformer import transform

def deleteFileFromFS(filename):
    file = mongo.db.fs.files.find_one({'filename': filename})
    mongo.db.fs.files.delete_one({'_id': file.get('_id')})
    mongo.db.fs.chunks.delete_many({'files_id': file.get('_id')})

def saveTempFileAndCleanup(temp_filepath, db_filename):
    mongo.save_file(db_filename, open(temp_filepath, 'rb'))
    os.remove(temp_filepath)

class User:
    @staticmethod
    def login(username: str, password: str) -> Tuple[int, str, dict]:
        users = mongo.db.users

        # Verify user exists
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist', {}

        # Verify user's account password
        if not pbkdf2_sha256.verify(password, found_user.get(USER_DOCUMENT_KEYS.PASSWORD_HASH)):
            return 401, 'Password provided is incorrect', {}

        # Generate access tokens
        access_token = create_access_token(identity=username)
        return 200, f'User {username} logged in', { 'access_token': access_token }
    
    @staticmethod
    def register(username, password) -> Tuple[int, str]:
        # Verify user does not exist
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if found_user:
            return 409, 'User already exists'
        
        # Create a User document
        new_user = {
            USER_DOCUMENT_KEYS.USERNAME: username,
            USER_DOCUMENT_KEYS.PASSWORD_HASH: pbkdf2_sha256.hash(password),
            USER_DOCUMENT_KEYS.IMAGES: []
        }
        users.insert_one(new_user) # Add to DB
        return 200, f'User {username} was created.'

    @staticmethod
    def save_video(username, videoFile) -> Tuple[int, str]:
        # Verify if file is valid
        file_extension = get_file_extension(videoFile.filename)
        if not file_extension in ALLOWED_VIDEO_EXTENSIONS:
            return 400, f'Invalid file provided. Acceptable extensions are: {", ".join(ALLOWED_VIDEO_EXTENSIONS)}'

        # Find user
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist'
        
        # Store video on server
        unique_file_prefix = str(uuid.uuid4())
        db_filepath = f'{unique_file_prefix}.{file_extension}'
        mongo.save_file(db_filepath, videoFile)

        # Update user document with filename
        result = users.update_one({USER_DOCUMENT_KEYS.USERNAME: username}, {'$push': {USER_DOCUMENT_KEYS.VIDEOS: db_filepath}})

        return 200, f'Video was successfully saved'

    @staticmethod
    def get_video_names(username, limit=None, offset=0) -> Tuple[int, str, list]:
        # Find user
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist', None
        
        # Get list of video filenames for the user
        filenames = found_user.get(USER_DOCUMENT_KEYS.VIDEOS, [])
        
        # Adjust response according to pagination config
        result = filenames
        if limit:
            result = filenames[int(offset):int(limit)]
        return 200, f'{len(result)} filename(s)', result

    @staticmethod
    def delete_video(username, video_name) -> Tuple[int, str]:
        # TODO Update this endpoint according to schema changes
        # Find user
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist'
        
        # Verify if video_name exists
        result = users.update_one({ '_id': found_user.get('_id')}, { '$pull': { USER_DOCUMENT_KEYS.VIDEOS: video_name}})
        
        # Delete file
        deleteFileFromFS(video_name)

        # Return success 
        return 200, f'Video were deleted successfully.'
        