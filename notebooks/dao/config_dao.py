import json

from notebooks import db

SERVER_SELECT = "select settings from discord_server where server_cod=%s;"


def get_all_config(server_cod):
    data = db.make_select(SERVER_SELECT, [server_cod])
    if len(data) == 0:
        raise Exception("Invalid Server Cod")
    return json.loads(data[0]['settings'])


def get_config(server_cod, config):
    return get_all_config(server_cod).get(config)


if __name__ == '__main__':
    pass