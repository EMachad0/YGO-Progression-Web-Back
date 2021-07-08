from notebooks import db


def get_player_cod(user_cod, server_cod):
    player_select = "select player_cod from player where server_cod=%s and user_cod=%s;"
    data = db.make_select(player_select, (server_cod, user_cod))
    if len(data) == 0:
        raise KeyError("No player found")
    return data[0]['user_cod']