from app.app import db
from app.models import DiscordUser


def insert_discord_user(user_cod, name, discriminator, img_url):
    ins = db.insert(DiscordUser).values(user_cod=user_cod, name=name, discriminator=discriminator, img_url=img_url). \
        on_conflict_do_update(index_elements=[DiscordUser.user_cod],
                              set_={'name': name, 'discriminator': discriminator})
    db.session.execute(ins)
    db.session.commit()


def get_discord_user(user_cod):
    return db.session.query(DiscordUser).get(user_cod)


def drop_discord_user(user_cod):
    db.session.query(DiscordUser).filter(DiscordUser.user_cod == user_cod).delete()
    db.session.commit()
