from flask import Flask
from .routes import comment_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.register_blueprint(comment_routes)
    return app
