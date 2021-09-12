import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


def create_app():
    _app = Flask(__name__)
    _app.secret_key = os.environ['SECRET_KEY']
    CORS(_app)
    return _app


def config_db(_app):
    _app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    _db = SQLAlchemy(_app)
    return _app, _db


def register_routes(_app):
    from app.routes import blueprints
    for blue in blueprints:
        _app.register_blueprint(blue)
    return _app


app = create_app()
app, db = config_db(app)
app = register_routes(app)


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
