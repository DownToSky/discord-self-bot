import discord
from discord.ext import commands
from elizabeth_the_third.add_text import elizabeth_cat
import json
import asyncio
import os

CRED_PATH = os.path.abspath("cred")
EMAIL_PATH = os.path.join(CRED_PATH, "email.txt")
PASS_PATH = os.path.join(CRED_PATH, "pass.txt")

description = "```A self bot with a lot of utility commands and functionality. Mainly trying to not attract attetion of your fellow chatters```"

credentials = {"email" : "",
        "password" : "",
        }

# Get maximume lenght matching quote string
def _gmlmqs_(string):
    q1 = 0
    q2 = len(string) - 1
    for q1 in range(q1, len(string)):
        if string[q1] is "\"":
            break
    for q2 in range(q2, q1, -1):
        if string[q2] is "\"":
            break
    return string[(q1 + 1):q2]

#WARNING: this needs to use OS.PATH!
def get_credentials():
    with open("cred/email.txt", 'r') as email_f:
        txt = email_f.read()
        credentials["email"] = _gmlmqs_(txt)

    with open("cred/pass.txt", 'r') as password_f:
        txt = password_f.read()
        credentials["password"] = _gmlmqs_(txt)

bot = commands.Bot(command_prefix = '%', description = description,
        self_bot=True)
bot.cat = elizabeth_cat()

@bot.command(name = "elizabeth", pass_context=True, no_pm=True)
async def send_elizabeth_message(ctx, ID:str, *, msg:str):
    if ctx.message.channel.id == "343159135082250243":
        all_channels = list()
        for server in bot.servers:
            all_channels += server.channels
        dest = discord.utils.get(all_channels, id=ID)
        bot.cat.create_text(0, msg, rand=True)
        pic_path = os.path.abspath("elizabeth_the_third/tmp.png")
        with open(pic_path, 'rb') as f:
            await bot.send_file(dest, f)
        bot.cat.delete_tmp()



@bot.event
async def on_ready():
    user_name = bot.user.name.encode("ascii").decode("ascii")
    print("Logged in as")
    print(user_name)
    print(bot.user.id)

async def status_upkeep_task():
    await bot.wait_until_ready()
    while not bot.is_closed:
        await bot.change_presence(game=discord.Game(name="Discord is using me :("), status=discord.Status.dnd)
        await asyncio.sleep(10)


get_credentials()
bot.loop.create_task(status_upkeep_task())
bot.run(credentials["email"], credentials["password"])
