import json
import os
from imageTransformer.constants import ALLOWED_IMAGE_EXTENSIONS

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from imageTransformer.app import app, mongo
from imageTransformer.constants import REQUEST_KEYS, TRANSFORMED_FILE_PREFIX
from imageTransformer.models import User
from imageTransformer.helpers import getMissingArgs, saveTempFileAndCleanup, get_file_extension
from sampleTransformer import transform

@app.route('/videos/<video_name>',methods=['GET'])
@jwt_required()
def get_video(video_name):
    filename = video_name
    return mongo.send_file(filename)
    
@app.route('/videos', methods=['GET'])
@jwt_required()
def get_video_names():
    username = get_jwt_identity()
    limit = request.args.get('limit', None)
    offset = request.args.get('offset', 0)
    status, message, data = User.get_video_names(username, limit, offset)
    return jsonify({'msg': message, 'data': data}), status

@app.route('/videos', methods=['POST'])
@jwt_required()
def save_video():
    # Verify required arguments
    missingArgs = getMissingArgs(request.files, [REQUEST_KEYS.VIDEO])
    if missingArgs:
        return jsonify({'msg': f'Missing required argument(s): {", ".join(missingArgs)}'}), 400
    
    status, message = User.save_video(get_jwt_identity(), request.files[REQUEST_KEYS.VIDEO])
    return jsonify({'msg': message}), status

@app.route('/videos/<video_name>', methods=['DELETE'])
@jwt_required()
def delete_image(video_name):
    username = get_jwt_identity()
    status, message = User.delete_video(username, video_name)
    return jsonify({'msg': message}), status

@app.route('/transform', methods=['POST'])
def transform_image():
    # Verify required arguments
    missingArgs = getMissingArgs(request.files, [REQUEST_KEYS.IMAGE])
    if missingArgs:
        return jsonify({'msg': f'Missing required argument(s): {", ".join(missingArgs)}'}), 400
    
    # Verify if file is valid
    file_extension = get_file_extension(request.files[REQUEST_KEYS.IMAGE].filename)
    if not file_extension in ALLOWED_IMAGE_EXTENSIONS:
        return jsonify({'msg': f'Invalid image provided. Acceptable extensions are: {", ".join(ALLOWED_IMAGE_EXTENSIONS)}'}), 400
    success, transformed_temp_filepath = transform(request.files[REQUEST_KEYS.IMAGE])
    
    #TODO Error Handling with success
    if not success:
        return jsonify({'msg': f'Transformation failed for the image'}), 500

    # Save file in DB and clean up temporary one
    db_filepath = f'unlinked-{transformed_temp_filepath}'
    saveTempFileAndCleanup(transformed_temp_filepath, db_filepath) #TODO file will be deleted later periodically

    return mongo.send_file(db_filepath)