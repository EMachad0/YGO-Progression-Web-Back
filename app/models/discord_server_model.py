from app.app import db


class DiscordServer(db.Model):
    server_cod = db.Column(db.BigInteger, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(100))
    img_url = db.Column(db.String(500))
    settings = db.Column(db.Text)
