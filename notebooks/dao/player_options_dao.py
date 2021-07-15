from app import db
from sqlalchemy.dialects.postgresql import JSONB


class PlayerOptions(db.Model):
    __table__ = db.Table('player_options', db.metadata,
                         db.Column('player_cod', db.Integer, db.ForeignKey('player.player_cod'), primary_key=True),
                         db.Column('types', JSONB),
                         db.Column('attributes', JSONB),
                         db.Column('races', JSONB),
                         db.Column('archetypes', JSONB),
                         db.Column('sets', JSONB),
                         db.Column('rarities', JSONB),
                         db.Column('card_total', db.BigInteger))


def get_player_options(player_cod):
    return db.session.query(PlayerOptions).get(player_cod)
