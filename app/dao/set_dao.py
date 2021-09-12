from app.app import db
from app.models import Set, Collection, Pull


def get_set(set_cod):
    return db.session.query(Set).get(set_cod)


def get_all_sets():
    return db.session.query(Set).order_by(Set.release_date).all()


def get_player_sets(player_cod):
    sub = db.session.query(Pull.set_cod).join(Collection, Pull.pull_cod == Collection.pull_cod) \
        .filter(Collection.player_cod == player_cod).subquery()
    return db.session.query(Set).join(sub, Set.set_cod == sub.c.set_cod).order_by(Set.release_date).all()
