from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from imageTransformer.app import app, mongo
from imageTransformer.constants import REQUEST_KEYS, TRANSFORMED_FILE_PREFIX
from imageTransformer.models import User
from imageTransformer.routes.helpers import getMissingArgs

@app.route('/images/<image_name>',methods=['GET'])
@app.route('/images/<image_name>/<transformed>', methods=['GET'])
def get_image(image_name, transformed=False):
    filename = image_name
    if transformed:
        filename = TRANSFORMED_FILE_PREFIX + filename
    return mongo.send_file(filename)
    
@app.route('/images', methods=['GET'])
@jwt_required()
def get_images():
    username = get_jwt_identity()
    limit = request.args.get('limit', None)
    offset = request.args.get('offset', 0)
    status, message, data = User.get_image_names(username, limit, offset)
    return jsonify({'msg': message, 'data': data}), status

@app.route('/images', methods=['POST'])
@jwt_required()
def add_image():
    # Verify required arguments
    missingArgs = getMissingArgs(request.files, [REQUEST_KEYS.IMAGE])
    if missingArgs:
        return jsonify({'msg': f'Missing required argument(s): {", ".join(missingArgs)}'}), 400
    
    status, message = User.add_image(get_jwt_identity(), request.files[REQUEST_KEYS.IMAGE])
    return jsonify({'msg': message}), status

@app.route('/images/<image_name>', methods=['DELETE'])
@jwt_required()
def delete_image(image_name):
    username = get_jwt_identity()
    status, message = User.delete_image(username, image_name)
    return jsonify({'msg': message}), status
