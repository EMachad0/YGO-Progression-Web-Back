import json

from flask import Blueprint

from notebooks.dao import set_dao, utils

blue = Blueprint('set', __name__, static_folder="static", template_folder="templates")


@blue.route('/set/all_sets')
def all_sets():
    sets = set_dao.get_all_sets()
    sets = [utils.row2dict(s) for s in sets]
    return json.dumps(sets)
