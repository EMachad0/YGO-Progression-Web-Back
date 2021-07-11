from app import db


class Pull(db.Model):
    pull_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    card_cod = db.Column(db.Integer, db.ForeignKey('card.card_cod'))
    set_cod = db.Column(db.String(3), db.ForeignKey('set.set_cod'))
    rarity = db.Column(db.String(100))
    rarity_code = db.Column(db.String(100))
    price = db.Column(db.String(30))
