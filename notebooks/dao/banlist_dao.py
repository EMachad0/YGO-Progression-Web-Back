import json

from notebooks import db


def get_banlist_by_cod(banlist_cod):
    banlist_select = """select list from banlist where banlist_cod=%s;"""
    row = db.make_select(banlist_select, [banlist_cod])
    if len(row) == 0:
        raise KeyError("Invalid banlist_cod")
    return json.loads(row[0]['list'])


def get_banlist_by_date(release_date):
    banlist_select = """select list from banlist where release_date=%s;"""
    row = db.make_select(banlist_select, [release_date])
    if len(row) == 0:
        raise KeyError("Invalid release_date")
    return json.loads(row[0]['list'])
    
    