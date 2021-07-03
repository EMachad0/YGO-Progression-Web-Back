from flask import Blueprint, redirect, url_for, render_template

from notebooks import db

blue = Blueprint('deck_builder', __name__, static_folder="static", template_folder="templates")

PLAYER_SELECT = "select player_cod from player where user_cod=%s and server_cod=%s;"
COLLECTION_SELECT = "select * from (select pull_cod, quantity from collection where player_cod=%s) c " \
                    "join pull p on p.pull_cod = c.pull_cod " \
                    "join card cd on cd.card_cod = p.card_cod;"

@blue.route('/<guild>/<user>')
def deck_builder(guild, user):
    player = db.make_select(PLAYER_SELECT, (user, guild))
    if len(player) == 0:
        return redirect(url_for("login.login"))
    player = player[0]

    cards = db.make_select(COLLECTION_SELECT, [player['player_cod']])
    cards_json = {c['card_cod']: c for c in cards}
    return render_template('deck_builder.html', cards=cards, cards_json=cards_json, guild=guild, user=user)
