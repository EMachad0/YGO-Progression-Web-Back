from app.app import db
from app.models import Opening, Set, SetType


def insert_opening(values, quantity):
    ins = db.insert(Opening).values(values). \
        on_conflict_do_update(index_elements=[Opening.set_cod, Opening.player_cod],
                              set_={'quantity': Opening.quantity + quantity})
    db.session.execute(ins)
    db.session.commit()


def update_opening(open_cod, values):
    db.session.query(Opening).filter(Opening.open_cod == open_cod).update(values)
    db.session.commit()


def get_player_available_openings(player_cod):
    return db.session.query(Opening.open_cod, Opening.set_cod, Opening.quantity). \
        filter(Opening.player_cod == player_cod, Opening.quantity > 0) \
        .join(Set, Opening.set_cod == Set.set_cod) \
        .order_by(Set.release_date).all()


def get_openings_by_player(player_cod):
    return db.session.query(Opening.set_cod, Opening.open_cod, Opening.quantity, SetType.num_cards, SetType.list) \
        .join(Set, Opening.set_cod == Set.set_cod) \
        .join(SetType, Set.type_cod == SetType.set_type_cod) \
        .filter(Opening.player_cod == player_cod, Opening.quantity > 0) \
        .order_by(Set.release_date).first()


def get_opening_by_set_player(set_cod, player_cod):
    return db.session.query(Opening.open_cod, Opening.quantity, SetType.num_cards, SetType.list) \
        .join(Set, Opening.set_cod == Set.set_cod) \
        .join(SetType, Set.type_cod == SetType.set_type_cod) \
        .filter(Opening.player_cod == player_cod, Set.set_cod == set_cod, Opening.quantity > 0).first()
