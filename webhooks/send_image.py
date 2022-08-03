from discord_webhook import DiscordWebhook
from datetime import datetime
import links #import your own webhook links like this:  link_to_edited = 'url_of_webhook_here'

# creating image name from unix timestamp
image_name = str(int(datetime.timestamp(datetime.now()))) + '-käsitelty-kuva' + '.jpg'

# path to image
path_to_image = "/home/b9/portfolio/discord/radio-kuvankasittely/Touchdesigner/kuva1.jpg"

# get the webhook link for webhook
webhook = DiscordWebhook(url=links.link_to_edited, username="Automaaginen kuvankäsittelijä 1.0")

# send one image
with open(path_to_image, "rb") as f:
    webhook.add_file(file=f.read(), filename=image_name)

## send two images
#with open(path_to_image, "rb") as f:
#    webhook.add_file(file=f.read(), filename='käsitelty1.jpg')
#with open("/home/b9/portfolio/discord/radio-kuvankasittely/Touchdesigner/kuva2.jpg", "rb") as f:
#    webhook.add_file(file=f.read(), filename='käsitelty2.jpg')

response = webhook.execute()