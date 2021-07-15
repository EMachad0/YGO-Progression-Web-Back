from app import db


class Collection(db.Model):
    collection_cod = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    player_cod = db.Column(db.Integer, db.ForeignKey('player.player_cod'))
    pull_cod = db.Column(db.Integer, db.ForeignKey('pull.pull_cod'))
    quantity = db.Column(db.Integer)


def get_player_collection(player_cod, offset=None, limit=None, name_filter=None, text_filter=None, set_filter=None,
                          rarity_filter=None, sorts=None, filters=None):
    from notebooks.filters import apply_sort, apply_filter
    from notebooks.dao import Card, UniquePulls

    sub = db.session.query(UniquePulls).filter(UniquePulls.player_cod == player_cod).subquery()
    query = db.session.query(Card.card_cod, Card.name, Card.atk, Card.dff, Card.level, Card.cod_img, Card.type,
                             Card.level, Card.scale, Card.link_val, Card.race, Card.attribute, sub.c.quantity) \
        .join(sub, sub.c.card_cod == Card.card_cod)
    if name_filter is not None:
        query = query.filter(Card.name.ilike(name_filter))
    if text_filter is not None:
        query = query.filter(Card.flavour_text.ilike(text_filter))
    if set_filter is not None:
        query = query.filter(sub.c.sets.comparator.contains([set_filter]))
    if rarity_filter is not None:
        query = query.filter(sub.c.rarities.comparator.contains([rarity_filter]))
    query = apply_sort(query, sorts)
    query = apply_filter(query, filters)
    query = query.offset(offset).limit(limit)
    # print(query.cte())
    return query.all()
