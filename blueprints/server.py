import json

from flask import Blueprint

from notebooks import utils
from notebooks.dao import discord_server_dao

blue = Blueprint('server', __name__, static_folder="static", template_folder="templates")


@blue.route('/server/all_servers')
def all_servers():
    guilds = discord_server_dao.get_all_servers()
    guilds = [utils.row2dict(s) for s in guilds]
    return json.dumps(guilds)
