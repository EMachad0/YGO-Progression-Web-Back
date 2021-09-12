import json

from app.dao.discord_server_dao import get_discord_server


def get_server_settings(server_cod):
    settings = get_discord_server(server_cod).settings
    return json.loads(settings)


def get_config(server_cod, config):
    return get_server_settings(server_cod).get(config)