from app.app import db


class Collection(db.Model):
    collection_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    player_cod = db.Column(db.Integer, db.ForeignKey('player.player_cod'))
    pull_cod = db.Column(db.Integer, db.ForeignKey('pull.pull_cod'))
    quantity = db.Column(db.Integer)
