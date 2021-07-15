from app import db


class SetType(db.Model):
    set_type_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    num_cards = db.Column(db.Integer)
    list = db.Column(db.Text)
