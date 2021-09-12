import json

from flask import Blueprint

from app.notebooks import utils
from app.dao import discord_server_dao

blue = Blueprint('server', __name__, static_folder="static", template_folder="templates")


@blue.route('/server/all_servers')
def all_servers():
    guilds = discord_server_dao.get_all_servers()
    guilds = [utils.row2dict(s) for s in guilds]
    for guild in guilds:
        guild["server_cod"] = str(guild["server_cod"])
    return json.dumps(guilds)
