import json

from flask import Blueprint, request, redirect, url_for, render_template

from notebooks import banlist_utils, images
from notebooks.dao import player_dao, collection_dao

blue = Blueprint('collection', __name__, static_folder="static", template_folder="templates")

# collection/823962832583655424/203615933539942400

@blue.route('/<guild>/<user>')
def collection(guild, user):
    player = player_dao.get_player_by_user_server(user, guild)
    if player is None:
        return redirect(url_for("login.login"))
    print(guild, user)
    return render_template('collection.html', guild=guild, user=user)


@blue.route('/')
def collection_card_list():
    params = request.args
    if params.get('guild') is None or params.get('user') is None:
        return "{'error': 'No User or guild'}"

    player = player_dao.get_player_by_user_server(params['user'], params['guild'])
    if player is None:
        return "{'error': 'Invalid Player'}"

    cards = collection_dao.get_player_collection(player.player_cod, params.get('offset'), params.get('limit'), params.get('name_filter'))
    ban_list = banlist_utils.get_guild_banlist(params['guild'])

    cards = [dict(c) for c in cards]
    for c in cards:
        c['limit'] = ban_list.get(c['name'])
        if c.get('limit') is None:
            images.get_img(c['cod_img'])
        else:
            images.get_img_banlist(c['cod_img'], c['limit'])
            c['cod_img'] = f"{c['cod_img']}_{c['limit']}"

    cards_json = {c['card_cod']: c for c in cards}
    return json.dumps(cards_json)
