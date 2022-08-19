from filters import filters
from PIL import Image, ImageFilter
from PIL import ImageFont, ImageDraw
from discord_webhook import DiscordWebhook
from decouple import config
import io

DCWEBHOOK1  = config('DCWEBHOOK1')


def send(img):
    img = img
    edited = filters.ImageMagic.quantize(img, 3)
    edited.convert('RGB').save("./images/edited.jpg")
    webhook = DiscordWebhook(url=DCWEBHOOK1, username="Automaaginen kuvankäsittelijä 1.0")

    with io.open("./images/edited.jpg", "rb") as f:
        webhook.add_file(file=f.read(), filename="edited.jpg")
        f.close()
    webhook.execute()
    return