from app.app import db


class Opening(db.Model):
    open_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    set_cod = db.Column(db.String(3), db.ForeignKey('set.set_cod'))
    player_cod = db.Column(db.Integer, db.ForeignKey('player.player_cod'))
    quantity = db.Column(db.Integer)
