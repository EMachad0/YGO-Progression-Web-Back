from app.app import db
from app.models import Player, DiscordUser


def get_player_by_user_server(user_cod, server_cod):
    return Player.query.filter(Player.user_cod == user_cod, Player.server_cod == server_cod).first()


def get_all_players_by_server(server_cod):
    return db.session.query(DiscordUser) \
        .join(Player, DiscordUser.user_cod == Player.user_cod) \
        .filter(Player.server_cod == server_cod).all()
