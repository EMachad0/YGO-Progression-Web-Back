from app import db


class Player(db.Model):
    player_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_cod = db.Column(db.BigInteger, db.ForeignKey('discord_user.user_cod'))
    server_cod = db.Column(db.BigInteger, db.ForeignKey('discord_server.server_cod'))


def get_player_by_user_server(user_cod, server_cod):
    return Player.query.filter(Player.user_cod == user_cod, Player.server_cod == server_cod).first()


def get_all_players_by_server(server_cod):
    from notebooks.dao import DiscordUser
    return db.session.query(DiscordUser) \
        .join(Player, DiscordUser.user_cod == Player.user_cod) \
        .filter(Player.server_cod == server_cod).all()
