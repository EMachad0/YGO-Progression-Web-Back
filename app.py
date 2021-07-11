import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Machado'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gbbukjnnxeolsm:ac0c65368870ba42501c292c93c21a96949c23837b0ab5c3102ce6e5819502f7@ec2-52-6-77-239.compute-1.amazonaws.com:5432/d7msjjetg6jff5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import blueprints
app.register_blueprint(blueprints.collection)

@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
