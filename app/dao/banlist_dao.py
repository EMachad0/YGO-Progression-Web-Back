from app.models import Banlist


def get_banlist(banlist_cod):
    return Banlist.query.get(banlist_cod)


def get_banlist_by_date(release_date):
    return Banlist.query.filter_by(release_date=release_date).first()
