from os.path import isfile

import requests
from PIL import Image

IMG_URL='https://storage.googleapis.com/ygoprodeck.com/pics/'
IMG_SMALL_URL='https://storage.googleapis.com/ygoprodeck.com/pics_small/'


def get_img_big(cod, overwrite=False):
    if isfile(f"static/img/card_images/{cod}.jpg") and not overwrite:
        return
    url = f"{IMG_URL}{cod}.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(f"static/img/card_images/{cod}.jpg", 'JPEG')


def get_img_small(cod, overwrite=False):
    if isfile(f"static/img/card_images_small/{cod}.jpg") and not overwrite:
        return
    url = f"{IMG_SMALL_URL}{cod}.jpg"
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(f"static/img/card_images_small/{cod}.jpg", 'JPEG')
    

def get_img(cod, overwrite=False):
    get_img_big(cod, overwrite)
    get_img_small(cod, overwrite)


def get_img_banlist_big(cod, limit, overwrite=False):
    if limit < 0 or limit > 2:
        return
    if isfile(f"static/img/card_images/{cod}_{limit}.jpg") and not overwrite:
        return
    get_img_big(cod)
    image = Image.open(f"static/img/card_images/{cod}.jpg")
    icon = Image.open(f"static/img/banlist-icons/{limit}-icon.png")
    image.paste(icon, (330, 100), icon)
    image.save(f"static/img/card_images/{cod}_{limit}.jpg", 'JPEG')
    

def get_img_banlist_small(cod, limit, overwrite=False):
    if limit < 0 or limit > 2:
        return
    if isfile(f"static/img/card_images_small/{cod}_{limit}.jpg") and not overwrite:
        return
    get_img_big(cod)
    image = Image.open(f"static/img/card_images_small/{cod}.jpg")
    icon = Image.open(f"static/img/banlist-icons/{limit}-icon.png")
    icon = icon.resize((32, 32))
    image.paste(icon, (130, 40), icon)
    image.save(f"static/img/card_images_small/{cod}_{limit}.jpg", 'JPEG')
    
    
def get_img_banlist(cod, limit, overwrite=False):
    get_img_banlist_big(cod, limit, overwrite)
    get_img_banlist_small(cod, limit, overwrite)
    
    
if __name__ == '__main__':
    get_img_banlist_small(66788016, 2, True)