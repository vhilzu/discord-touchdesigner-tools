<<<<<<< HEAD
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
=======
from discord_webhook import DiscordWebhook
from datetime import datetime
from decouple import config

DISCORD_DCKKWEBHOOK  = config('DCKKWEBHOOK')

# creating image name from unix timestamp
image_name = str(int(datetime.timestamp(datetime.now()))) + '-käsitelty-kuva' + '.jpg'

# path to image
path_to_image = "/home/b9/portfolio/discord/radio-kuvankasittely/Touchdesigner/kuva1.jpg"

# get the webhook link for webhook
webhook = DiscordWebhook(url=DISCORD_DCKKWEBHOOK, username="Automaaginen kuvankäsittelijä 1.0")

# send one image
with open(path_to_image, "rb") as f:
    webhook.add_file(file=f.read(), filename=image_name)

## send two images
#with open(path_to_image, "rb") as f:
#    webhook.add_file(file=f.read(), filename='käsitelty1.jpg')
#with open("/home/b9/portfolio/discord/radio-kuvankasittely/Touchdesigner/kuva2.jpg", "rb") as f:
#    webhook.add_file(file=f.read(), filename='käsitelty2.jpg')

response = webhook.execute()
>>>>>>> 0486e455207ca92a4a727a982d1e73f57a5e2b14
