import json
from datetime import datetime

from notebooks import config
from notebooks.dao import banlist_dao


def get_guild_banlist(server_cod):
    banlist_date = config.get_config(server_cod, "ban_list")
    # print(banlist_date)
    try:
        banlist_date = datetime.strptime(banlist_date, "%B %Y")
        banlist = banlist_dao.get_banlist_by_date(banlist_date)
        return json.loads(banlist.list)
    except (ValueError, KeyError):
        return {}
