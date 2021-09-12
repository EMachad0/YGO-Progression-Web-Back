import json

from flask import Blueprint, request

from app.notebooks import utils
from app.dao import player_dao

blue = Blueprint('player', __name__, static_folder="static", template_folder="templates")


@blue.route('/player/all_players')
def all_players():
    return {"TODO"}


@blue.route('/player/guild_players')
def guild_players():
    params = request.args
    if params.get('guild') is None:
        return "{'error': 'No guild'}"

    players = player_dao.get_all_players_by_server(params['guild'])
    players = [utils.row2dict(s) for s in players]
    for player in players:
        player["user_cod"] = str(player["user_cod"])
    return json.dumps(players)
