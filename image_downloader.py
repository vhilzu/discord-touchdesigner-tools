<<<<<<< HEAD:image_downloader.py
import discord
from discord.ext import commands
from colorama import Fore, Back, Style ## console colours
import datetime
import io, os, sys
from decouple import config
from discord_webhook import DiscordWebhook
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from webhooks import send_image
import edit_image

# keys and paths from env variables
TOOLAPPID  = config('DCTOOLAPPID')
TOOLTOKEN  = config('DCTOOLTOKEN')
PATHTOIMAGEFOLDER = config('PATHTOIMAGEFOLDER')
PATHTOTOUCHLOGFOLDER = config('PATHTOTOUCHLOGFOLDER')
DCWEBHOOK1  = config('DCWEBHOOK1')


BOT_Prefix=("!")
client = commands.Bot(command_prefix=BOT_Prefix)
client.remove_command("help")

@client.command()
async def help(ctx):
    author = ctx.message.author

    helpembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    helpembed.set_author(name="Help")
    helpembed.add_field(name="d.ping", value = "Standard ping pong command", inline=False)
    await ctx.send(embed=helpembed)

print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + " attempting to establish connection to the client")

@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://github.com/vhilzu/discord-touchdesigner-tools",
                                 name=f"ufopornoo \../") #This is the bots status. You can edit what this says between the " " 
    await client.change_presence(status=discord.Status.online, activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established, logged in as: " + client.user.name)

image_types = ["png", "jpeg", "gif", "jpg", "mp4", "mov"] #You can add more attachments/formats here to be saved.
image_name = []


## IF the channel is #kuvat-jotka-kaipaavat-vesileimaa
## copy the attachment to PATHTOIMAGEFOLDER and log the message to PATHTOTOUCHLOGFOLDER
@client.event
async def on_message(message: discord.Message):
    if message.channel.id == 1003650595942584401 and message.webhook_id != 1004472875132141608:
        for attachment in message.attachments:
            if (attachment.filename.lower().endswith(image) for image in image_types):
                await attachment.save(f'{PATHTOIMAGEFOLDER}{attachment.filename}')
                print('saved')
                print(Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + f'Attachment {attachment.filename} has been saved to directory/folder > attachments.')
        else:
            if message.channel.id == 1003650595942584401 and message.webhook_id != 1004472875132141608:
                img = Image.open(PATHTOIMAGEFOLDER + attachment.filename)
                edit_image.send(img)
            with io.open(PATHTOTOUCHLOGFOLDER + "/logs.txt", "a", encoding="utf-8") as f: #if logs.txt doesn't exist, it will create it and write to it.
                    f.write(
                        f"[{message.guild}] | [{message.channel}] | [{message.author}] @ {message.created_at}: {message.content}\n")
                    f.close()
            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"[{message.guild}] | [{message.channel}] | [{message.author}] @ {message.created_at}: {message.content}")
    await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")

#https://discordapp.com/oauth2/authorize?client_id=BOT_ID_HERE&scope=bot&permissions=8" permissions=8 = Admin Permissions in servers.
# (this can be edited to just read and send messages.) Although you won't save text or images in staff channels/private channels that admins can access.

client.run(TOOLTOKEN) 
=======
import discord
from discord.ext import commands
from colorama import Fore, Back, Style ## console colours
import datetime
import io
from decouple import config

# keys and paths from env variables
DISCORD_TOOLAPPID  = config('DCTOOLAPPID')
DISCORD_TOOLTOKEN  = config('DCTOOLTOKEN')
PATHTOTOUCHIMAGEFOLDER = config('PATHTOTOUCHIMAGEFOLDER')
PATHTOTOUCHLOGFOLDER = config('PATHTOTOUCHLOGFOLDER')

BOT_Prefix=("!")
client = commands.Bot(command_prefix=BOT_Prefix)
client.remove_command("help")

@client.command()
async def help(ctx):
    author = ctx.message.author

    helpembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    helpembed.set_author(name="Help")
    helpembed.add_field(name="d.ping", value = "Standard ping pong command", inline=False)
    await ctx.send(embed=helpembed)

print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + " attempting to establish connection to the client")

@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://github.com/vhilzu/discord-touchdesigner-tools",
                                 name=f"ufopornoo \../") #This is the bots status. You can edit what this says between the " " 
    await client.change_presence(status=discord.Status.online, activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established, logged in as: " + client.user.name)

image_types = ["png", "jpeg", "gif", "jpg", "mp4", "mov"] #You can add more attachments/formats here to be saved.

## IF the channel is #kuvat-jotka-kaipaavat-vesileimaa
## copy the attachment to PATHTOTOUCHIMAGEFOLDER and log the message to PATHTOTOUCHLOGFOLDER
@client.event
async def on_message(message: discord.Message):
    if message.channel.id == 1003650595942584401:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in image_types):
                await attachment.save(f'{PATHTOTOUCHIMAGEFOLDER} {attachment.filename}') # 'attachments/{{attachment.filename}' is the PATH to where the attachmets/images will be saved. Example: home/you/Desktop/attachments/{{attachment.filename}
                print(Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + f'Attachment {attachment.filename} has been saved to directory/folder > attachments.')
        else:
            if message.channel.id == 1003650595942584401:
                with io.open(PATHTOTOUCHLOGFOLDER + "/logs.txt", "a", encoding="utf-8") as f: #if logs.txt doesn't exist, it will create it and write to it.
                    f.write(
                        f"[{message.guild}] | [{message.channel}] | [{message.author}] @ {message.created_at}: {message.content}\n")
                    f.close()
            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"[{message.guild}] | [{message.channel}] | [{message.author}] @ {message.created_at}: {message.content}")
                
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")

#https://discordapp.com/oauth2/authorize?client_id=BOT_ID_HERE&scope=bot&permissions=8" permissions=8 = Admin Permissions in servers. (this can be edited to just read and send messages.) Although you won't save text or images in staff channels/private channels that admins can access.

client.run(DISCORD_TOOLTOKEN) 
>>>>>>> 0486e455207ca92a4a727a982d1e73f57a5e2b14:discord-bot/image_downloader.py
