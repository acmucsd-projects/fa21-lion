from flask import session
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from typing import * 

from imageTransformer.app import app, mongo
from imageTransformer.constants import UserDocumentKeys

class User:
    @staticmethod
    def login(username: str, password: str) -> (int, str, dict):
        users = mongo.db.users

        # Verify user exists
        found_user = users.find_one({UserDocumentKeys.username: username})
        if not found_user:
            return 404, 'User does not exist'

        # Verify user's account password
        if not pbkdf2_sha256.verify(password, found_user.get(UserDocumentKeys.passwordHash)):
            return 401, 'Password provided is incorrect'

        # Generate access tokens
        access_token = create_access_token(identity=username)
        return 200, f'User {username} logged in', { 'access_token': access_token }
    
    @staticmethod
    def register(fullname, username, password) -> (int, str):
        # Verify user does not exist
        users = mongo.db.users
        found_user = users.find_one({UserDocumentKeys.username: username})
        if found_user:
            return 409, 'User already exists'
        
        # Create a User document
        new_user = {
            UserDocumentKeys.username: username,
            UserDocumentKeys.fullname: fullname,
            UserDocumentKeys.passwordHash: pbkdf2_sha256.hash(password)
        }
        users.insert_one(new_user) # Add to DB

        return 200, f'User {username} was created.'