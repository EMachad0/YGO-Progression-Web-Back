from app.app import db
from app.models import PlayerOptions


def get_player_options(player_cod):
    return db.session.query(PlayerOptions).get(player_cod)
