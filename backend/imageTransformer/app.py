from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

from imageTransformer.config import DEVELOPMENT_CONFIG

def createApp():
    app = Flask(__name__)
    app.config.from_object(DEVELOPMENT_CONFIG)
    return app

app = createApp()
mongo = PyMongo(app)
jwt = JWTManager(app)

from imageTransformer.routes import *

