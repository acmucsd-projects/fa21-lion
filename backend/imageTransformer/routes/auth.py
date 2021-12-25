from flask import request, jsonify, session
from imageTransformer.models import User

from imageTransformer.app import app
from imageTransformer.constants import RequestKeys

@app.route('/login', methods=['POST'])
def login():
    # Sanity check for request format
    if not request.headers.get('Content-Type') == 'application/json':
        return jsonify({'msg': f'Expected json content type but found {request.headers.get("Content-Type")}'}), 400

    username = request.json.get(RequestKeys.username)
    password = request.json.get(RequestKeys.password)
    
    # Verify username and password are provided
    if not username or not password:
        return jsonify({'msg': 'Username or/and password is missing'}), 400
    
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
    
    fullname = request.json.get(RequestKeys.fullname)
    username = request.json.get(RequestKeys.username)
    password = request.json.get(RequestKeys.password)

    # Verfy all fields are provided
    if not username or not fullname or not password:
        return jsonify({'msg': 'All required fields were not provided for account creation'}), 400

    status, message = User.register(fullname, username, password)
    return jsonify({'msg': message}), status
