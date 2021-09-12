from app.app import db


class DiscordUser(db.Model):
    user_cod = db.Column(db.BigInteger, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(100))
    discriminator = db.Column(db.Integer)
    img_url = db.Column(db.String(500))
