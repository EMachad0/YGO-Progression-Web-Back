import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import blueprints
app.register_blueprint(blueprints.login)
app.register_blueprint(blueprints.collection, url_prefix="/collection")
# app.register_blueprint(blueprints.deck_builder, url_prefix="/deck_builder")

@app.route('/')
def index():
    from notebooks.dao import collection_dao
    
    sorts = [{'model':'Card', 'field': 'level', 'direction': 'desc', 'nulls': 'nullslast'},
             {'model':'Card', 'field': 'atk', 'direction': 'asc', 'nulls': None}]
    filters = [{'model':'Card', 'field': 'level', 'op': '<', 'value': 7},
               {'model':'Card', 'field': 'atk', 'op': '>=', 'value': 1000},
               {'model':'Card', 'field': 'level', 'op': '<=', 'value': 2000}]
    col = collection_dao.get_player_collection(16, offset=5, limit=5, name_filter='%r%', filters=filters, sorts=sorts)
    for c in col:
        print(c['name'], c['level'], c['atk'])
    return ""


if __name__ == '__main__':
    app.run(debug=True)
