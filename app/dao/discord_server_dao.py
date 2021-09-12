from app.models import DiscordServer


def get_discord_server(server_cod):
    return DiscordServer.query.get(server_cod)


def get_all_servers():
    return DiscordServer.query.all()
