import json

from flask import Blueprint, request

from notebooks import utils
from notebooks.dao import set_dao, player_dao

blue = Blueprint('set', __name__, static_folder="static", template_folder="templates")


@blue.route('/set/player')
def player_sets():
    params = request.args
    if params.get('guild') is None or params.get('user') is None:
        return "{'error': 'No User or guild'}"

    player = player_dao.get_player_by_user_server(params['user'], params['guild'])
    if player is None:
        return "{'error': 'Invalid Player'}"

    sets = set_dao.get_player_sets(player.player_cod)
    sets = [utils.row2dict(s) for s in sets]
    return json.dumps(sets)


@blue.route('/set/all_sets')
def all_sets():
    sets = set_dao.get_all_sets()
    sets = [utils.row2dict(s) for s in sets]
    return json.dumps(sets)
