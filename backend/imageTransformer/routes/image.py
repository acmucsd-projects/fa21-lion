from flask_jwt_extended import jwt_required, get_jwt_identity

from imageTransformer.app import app

@app.route('/image', methods=['GET'])
@jwt_required()
def getImages():
    #TODO Placeholder
    return f"All images for {get_jwt_identity()}"

