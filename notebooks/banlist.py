from notebooks.dao import config_dao, banlist_dao

from datetime import datetime

def get_guild_banlist(server_cod):
    banlist_date = config_dao.get_config(server_cod, "ban_list")
    try:
        banlist_date = datetime.strptime(banlist_date, "%B %Y")
        return banlist_dao.get_banlist_by_date(banlist_date)
    except (ValueError, KeyError):
        return {}
    
    
if __name__ == "__main__":
    print(get_guild_banlist("823962832583655424"))