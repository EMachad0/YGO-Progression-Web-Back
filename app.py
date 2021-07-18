import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

import blueprints

app.register_blueprint(blueprints.collection)
app.register_blueprint(blueprints.player)
app.register_blueprint(blueprints.server)
app.register_blueprint(blueprints.sett)


@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
