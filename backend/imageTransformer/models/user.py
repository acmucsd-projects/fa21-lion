from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from typing import * 
import uuid

from imageTransformer.app import app, mongo
from imageTransformer.constants import USER_DOCUMENT_KEYS, ALLOWED_EXTENSIONS, TRANSFORMED_FILE_PREFIX

from sampleTransformer import transform

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else None

def deleteFileFromFS(filename):
    file = mongo.db.fs.files.find_one({'filename': filename})
    mongo.db.fs.files.delete_one({'_id': file.get('_id')})
    mongo.db.fs.chunks.delete_many({'files_id': file.get('_id')})

class User:
    @staticmethod
    def login(username: str, password: str) -> Tuple[int, str, dict]:
        users = mongo.db.users

        # Verify user exists
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist'

        # Verify user's account password
        if not pbkdf2_sha256.verify(password, found_user.get(USER_DOCUMENT_KEYS.PASSWORD_HASH)):
            return 401, 'Password provided is incorrect'

        # Generate access tokens
        access_token = create_access_token(identity=username)
        return 200, f'User {username} logged in', { 'access_token': access_token }
    
    @staticmethod
    def register(fullname, username, password) -> Tuple[int, str]:
        # Verify user does not exist
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if found_user:
            return 409, 'User already exists'
        
        # Create a User document
        new_user = {
            USER_DOCUMENT_KEYS.USERNAME: username,
            USER_DOCUMENT_KEYS.FULLNAME: fullname,
            USER_DOCUMENT_KEYS.PASSWORD_HASH: pbkdf2_sha256.hash(password),
            USER_DOCUMENT_KEYS.IMAGES: []
        }
        users.insert_one(new_user) # Add to DB
        return 200, f'User {username} was created.'

    @staticmethod
    def add_image(username, imageFile) -> Tuple[int, str]:
        # Verify if file is valid
        file_extension = get_file_extension(imageFile.filename)
        if not file_extension in ALLOWED_EXTENSIONS:
            return 400, f'Invalid image provided. Acceptable extensions are: {", ".join(ALLOWED_EXTENSIONS)}'

        # Find user
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist'
        
        # Store original image on server
        unique_file_prefix = str(uuid.uuid4())
        original_filename = f'{unique_file_prefix}.{file_extension}'
        mongo.save_file(original_filename, imageFile)

        # Run model on image and store transformed image on server
        success, transformed_file = transform(imageFile) # TODO Replace with ML model
        if success:
            transformed_filename = f'{TRANSFORMED_FILE_PREFIX}{unique_file_prefix}.{file_extension}'
            mongo.save_file(transformed_filename, transformed_file)

        # Update user document with the filenames
        result = users.update_one({USER_DOCUMENT_KEYS.USERNAME: username}, {'$push': {USER_DOCUMENT_KEYS.IMAGES: {
            USER_DOCUMENT_KEYS.FILENAME: original_filename,
            USER_DOCUMENT_KEYS.TRANSFORMED: success,
        }}})

        return 200, f'Image was successfully uploaded{" and transformed" if success else ""}.'

    @staticmethod
    def get_image_names(username, limit=None, offset=0) -> Tuple[int, str, list]:
        # Find user
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist', None
        
        # Get list of image filenames for the user
        filenames = found_user.get(USER_DOCUMENT_KEYS.IMAGES, [])
        
        # Adjust response according to pagination config
        result = filenames
        if limit:
            result = filenames[int(offset):int(limit)]
        return 200, f'{len(result)} filename(s)', result

    @staticmethod
    def delete_image(username, image_name) -> Tuple[int, str]:
        # Find user
        users = mongo.db.users
        found_user = users.find_one({USER_DOCUMENT_KEYS.USERNAME: username})
        if not found_user:
            return 404, 'User does not exist'
        
        # Verify if image_name exists
        result = users.update_one({ '_id': found_user.get('_id')}, { '$pull': { USER_DOCUMENT_KEYS.IMAGES: {USER_DOCUMENT_KEYS.FILENAME: image_name}}})
        
        # Delete original image file
        deleteFileFromFS(image_name)

        # Delete transformed image file
        deleteFileFromFS(f'{TRANSFORMED_FILE_PREFIX}{image_name}')

        # Return success 
        return 200, f'Images were deleted successfully.'
        