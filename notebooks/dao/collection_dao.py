from sqlalchemy import asc

from app import db


class Collection(db.Model):
    collection_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    player_cod = db.Column(db.Integer, db.ForeignKey('player.player_cod'))
    pull_cod = db.Column(db.Integer, db.ForeignKey('pull.pull_cod'))
    quantity = db.Column(db.Integer)


def get_player_collection(player_cod, offset=None, limit=None, name_filter=None, sorts=None, filters=None):
    from notebooks.filters import apply_sort, apply_filter
    from notebooks.dao import Pull, Card
    
    query = db.session.query(Card.card_cod, Card.name, Card.atk, Card.level, Card.cod_img, Collection.quantity)\
        .join(Pull, Collection.pull_cod==Pull.pull_cod)\
        .join(Card, Pull.card_cod==Card.card_cod)\
        .filter(Collection.player_cod == player_cod)
    if name_filter is not None:
        query = query.filter(Card.name.ilike(name_filter))
    query = apply_sort(query, sorts)
    query = apply_filter(query, filters)
    query = query.order_by(asc('name'))
    query = query.offset(offset).limit(limit)
    # print(query.cte())
    return query.all()