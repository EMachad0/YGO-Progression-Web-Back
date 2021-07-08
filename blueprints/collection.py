from flask import Blueprint, redirect, url_for, render_template

from notebooks import db, banlist, images

blue = Blueprint('collection', __name__, static_folder="static", template_folder="templates")

# http://localhost:5000/collection/823962832583655424/203615933539942400#

PLAYER_SELECT = "select player_cod from player where user_cod=%s and server_cod=%s;"
COLLECTION_SELECT = "select c.card_cod, name, atk, def, cod_img, level, scale, link_val from (select pull_cod from collection where player_cod=%s) col " \
                    "join pull p on p.pull_cod = col.pull_cod " \
                    "join card c on c.card_cod = p.card_cod;"

@blue.route('/<guild>/<user>')
def collection(guild, user):
    player = db.make_select(PLAYER_SELECT, (user, guild))
    if len(player) == 0:
        return redirect(url_for("login.login"))
    player = player[0]

    cards = db.make_select(COLLECTION_SELECT, [player['player_cod']])
    ban_list = banlist.get_guild_banlist(guild)
    for c in cards:
        images.get_img(c['cod_img'])
        if c['name'] in ban_list:
            limit = ban_list[c['name']]
            images.get_img_banlist(c['cod_img'], limit)
            c['cod_img'] = f"{c['cod_img']}_{limit}"
            
    cards_json = {c['card_cod']: c for c in cards}
    return render_template('collection.html', cards=cards, cards_json=cards_json, guild=guild, user=user)


if __name__ == "__main__":
    car = db.make_select(COLLECTION_SELECT, [7])
    car = {c['card_cod']:c for c in car}
    print(car)