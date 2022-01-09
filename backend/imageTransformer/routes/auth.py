from flask import request, jsonify, session
from imageTransformer.models import User

from imageTransformer.app import app
from imageTransformer.constants import REQUEST_KEYS
from imageTransformer.helpers import getMissingArgs

@app.route('/login', methods=['POST'])
def login():
    # Sanity check for request format
    if not request.headers.get('Content-Type') == 'application/json':
        return jsonify({'msg': f'Expected json content type but found {request.headers.get("Content-Type")}'}), 400

    # Verify required arguments
    missingArgs = getMissingArgs(request.json, [REQUEST_KEYS.USERNAME, REQUEST_KEYS.PASSWORD])
    if missingArgs:
        return jsonify({'msg': f'Missing required argument(s): {", ".join(missingArgs)}'}), 400
    
    username = request.json.get(REQUEST_KEYS.USERNAME)
    password = request.json.get(REQUEST_KEYS.PASSWORD)
    
    status, message, tokens = User.login(username, password)

    return jsonify({'msg': message, 'tokens': tokens }), status
    
@app.route('/logout', methods=['POST'])
def logout():
    # TODO Assess importance of implamenting a blacklisting method for logging out
    return jsonify({'msg': 'Logged out successfully'}), 501

@app.route('/register', methods=['POST'])
def register():
    # Sanity check for request format
    if not request.headers.get('Content-Type') == 'application/json':
        return jsonify({'msg': f'Expected json content type but found {request.headers.get("Content-Type")}'}), 400
    
    # Verify required arguments
    missingArgs = getMissingArgs(request.json, [REQUEST_KEYS.USERNAME, REQUEST_KEYS.PASSWORD])
    if missingArgs:
        return jsonify({'msg': f'Missing required argument(s): {", ".join(missingArgs)}'}), 400
    
    username = request.json.get(REQUEST_KEYS.USERNAME)
    password = request.json.get(REQUEST_KEYS.PASSWORD)

    status, message = User.register(username, password)
    return jsonify({'msg': message}), status
