from app.app import db


class Set(db.Model):
    set_cod = db.Column(db.String(3), primary_key=True, nullable=False, unique=True)
    set_name = db.Column(db.String(100))
    num_of_cards = db.Column(db.Integer)
    release_date = db.Column(db.Date)
    type_cod = db.Column(db.Integer, db.ForeignKey('set_type.set_type_cod'))
