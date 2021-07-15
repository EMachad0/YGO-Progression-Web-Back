from app import db
from sqlalchemy.dialects.postgresql import JSONB


class UniquePulls(db.Model):
    __table__ = db.Table('unique_pulls', db.metadata,
                         db.Column('card_cod', db.Integer, db.ForeignKey('card.card_cod'), primary_key=True),
                         db.Column('player_cod', db.Integer, db.ForeignKey('player.player_cod'), primary_key=True),
                         db.Column('quantity', db.BigInteger),
                         db.Column('sets', JSONB),
                         db.Column('rarities', JSONB),
                         db.Column('price', db.Text))
