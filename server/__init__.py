from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from os import environ

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

    CORS(app, supports_credentials=True)

    from .testRoute import testRoute
    app.register_blueprint(testRoute, url_prefix='/testRoute')

    return app