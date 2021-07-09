from flask import Blueprint, redirect, url_for, render_template

from notebooks import banlist_utils, images
from notebooks.dao import db

blue = Blueprint('deck_builder', __name__, static_folder="static", template_folder="templates")

PLAYER_SELECT = "select player_cod from player where user_cod=%s and server_cod=%s;"
COLLECTION_SELECT = "select c.card_cod, name, type, atk, def, level, scale, race, attribute, cod_img, link_val, quantity from " \
                    "(select pull_cod, quantity from collection where player_cod=%s) col " \
                    "join pull p on p.pull_cod = col.pull_cod " \
                    "join card c on c.card_cod = p.card_cod;"


@blue.route('/<guild>/<user>')
def deck_builder(guild, user):
    player = db.make_select(PLAYER_SELECT, (user, guild))
    if len(player) == 0:
        return redirect(url_for("login.login"))
    player = player[0]

    cards = db.make_select(COLLECTION_SELECT, [player['player_cod']])
    ban_list = banlist_utils.get_guild_banlist(guild)
    for c in cards:
        images.get_img(c['cod_img'])
        if c['name'] in ban_list:
            limit = ban_list[c['name']]
            images.get_img_banlist(c['cod_img'], limit)
            c['cod_img'] = f"{c['cod_img']}_{limit}"
            
    cards_json = {c['card_cod']: c for c in cards}
    return render_template('deck_builder.html', cards=cards, cards_json=cards_json, guild=guild, user=user, banlist=ban_list)
