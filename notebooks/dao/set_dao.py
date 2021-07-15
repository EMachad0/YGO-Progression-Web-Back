from app import db


class Set(db.Model):
    set_cod = db.Column(db.String(3), primary_key=True, nullable=False, unique=True)
    set_name = db.Column(db.String(100))
    num_of_cards = db.Column(db.Integer)
    release_date = db.Column(db.Date)
    type_cod = db.Column(db.Integer, db.ForeignKey('set_type.set_type_cod'))


def get_set(set_cod):
    return db.session.query(Set).get(set_cod)


def get_all_sets():
    return db.session.query(Set).order_by(Set.release_date).all()


def get_player_sets(player_cod):
    from notebooks.dao import Collection, Pull
    sub = db.session.query(Pull.set_cod).join(Collection, Pull.pull_cod == Collection.pull_cod) \
        .filter(Collection.player_cod == player_cod).subquery()
    return db.session.query(Set).join(sub, Set.set_cod == sub.c.set_cod).order_by(Set.release_date).all()
