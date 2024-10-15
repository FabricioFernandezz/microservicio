from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    from app.resources import helloWorld
    app.register_blueprint(helloWorld.hello_world, url_prefix='/api/v1')

    return app