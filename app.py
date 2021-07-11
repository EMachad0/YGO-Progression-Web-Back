import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Machado'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import blueprints
app.register_blueprint(blueprints.collection)

@app.route('/')
def index():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
