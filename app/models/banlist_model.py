from app.app import db


class Banlist(db.Model):
    banlist_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    release_date = db.Column(db.Date, nullable=False, unique=True)
    list = db.Column(db.Text)
