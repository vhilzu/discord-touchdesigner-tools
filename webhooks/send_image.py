from discord_webhook import DiscordWebhook
from datetime import datetime
from decouple import config
DCWEBHOOK1  = config('DCWEBHOOK1')

def send_image():
    webhook = DiscordWebhook(url=DCWEBHOOK1, username="Automaaginen kuvankäsittelijä 1.0")
    image_name = '1.jpg'
    path_to_image="/home/b9/Desktop/TD/images/1.jpg"
    with open(path_to_image, "rb") as f:
        webhook.add_file(file=f.read(), filename=image_name)
    response = webhook.execute()