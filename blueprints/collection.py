import json

from flask import Blueprint, request

from notebooks import banlist_utils, utils
from notebooks.dao import player_dao, collection_dao, player_options_dao

blue = Blueprint('collection', __name__, static_folder="static", template_folder="templates")


@blue.route('/collection/')
def collection():
    params = request.args
    if params.get('guild') is None or params.get('user') is None:
        return "{'error': 'No User or guild'}"

    player = player_dao.get_player_by_user_server(params['user'], params['guild'])
    if player is None:
        return "{'error': 'Invalid Player'}"

    direction = params['dir'] if params.get('dir') is not None else 'asc'

    sorts = []
    if params.get('field') is not None:
        sorts = [{'model': 'Card', 'field': params['field'], 'direction': direction, 'nulls': 'nullslast'}]
    if params.get('field') != 'Name':
        sorts.append({'model': 'Card', 'field': 'name', 'direction': 'asc', 'nulls': 'nullslast'})

    cards = collection_dao.get_player_collection(player.player_cod, params.get('offset'), params.get('limit'),
                                                 params.get('name'), params.get('text'), params.get('set'),
                                                 params.get('rarity'), sorts=sorts)
    ban_list = banlist_utils.get_guild_banlist(params['guild'])

    cards = [dict(c) for c in cards]
    for c in cards:
        c['limit'] = ban_list.get(c['name'])
    return json.dumps(cards)


@blue.route('/collection/player_option')
def collection_player_option():
    params = request.args
    if params.get('guild') is None or params.get('user') is None:
        return "{'error': 'No User or guild'}"

    player = player_dao.get_player_by_user_server(params['user'], params['guild'])
    if player is None:
        return "{'error': 'Invalid Player'}"

    option = player_options_dao.get_player_options(player.player_cod)
    return json.dumps(utils.row2dict(option)).replace(', null', '')
