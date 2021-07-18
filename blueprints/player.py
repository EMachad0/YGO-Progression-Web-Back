import json

from flask import Blueprint, request

from notebooks import utils
from notebooks.dao import player_dao

blue = Blueprint('player', __name__, static_folder="static", template_folder="templates")


@blue.route('/player/all_players')
def all_servers():
    params = request.args
    if params.get('guild') is None:
        return "{'error': 'No guild'}"

    players = player_dao.get_all_players_by_server(params['guild'])
    players = [utils.row2dict(s) for s in players]
    return json.dumps(players)
