import json

from flask import Blueprint, request

from notebooks import banlist_utils
from notebooks.dao import player_dao, collection_dao

blue = Blueprint('collection', __name__, static_folder="static", template_folder="templates")


@blue.route('/')
def collection():
    params = request.args
    if params.get('guild') is None or params.get('user') is None:
        return "{'error': 'No User or guild'}"

    player = player_dao.get_player_by_user_server(params['user'], params['guild'])
    if player is None:
        return "{'error': 'Invalid Player'}"

    sorts = [{'model': 'Card', 'field': params.get('field'), 'direction': params.get('dir'), 'nulls': 'nullslast'}]

    cards = collection_dao.get_player_collection(player.player_cod, params.get('offset'), params.get('limit'),
                                                 params.get('name'), sorts=sorts)
    ban_list = banlist_utils.get_guild_banlist(params['guild'])

    cards = [dict(c) for c in cards]
    for c in cards:
        c['limit'] = ban_list.get(c['name'])
    return json.dumps(cards)