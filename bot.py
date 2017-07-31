import discord
from discord.ext import commands
import json

description = "```A self bot with a lot of utility commands and functionality. Mainly trying to not attract attetion of your fellow chatters```"

credentials = {"email" : "",
        "password" : "",
        }

# Get maximume lenght matching quote string
def gmlmqs(string):
    q1 = 0
    q2 = len(string) - 1
    for q1 in range(q1, len(string)):
        if string[q1] is "\"":
            break
    for q2 in range(q2, q1 -1, -1):
        if string[q2] is "\"":
            break

#WARNING: this needs to use OS.PATH!
def get_credentials():
    with open("cred/email.txt", 'r') as email_f:
        txt = email_f.read()
        credentials["email"] = gmlmqs(txt)

    with open("cred/pass.txt", 'r') as password_f:
        txt = password_f.read()
        credentials["password"] = gmlmqs(txt)

bot = commands.Bot(command_prefix = '@', description = description)


@bot.event
async def on_read():
    user_name = bot.user.name.encode("utf8")
    print("Logged in as")
    print(user_name)
    print(bot.user.id)

bot.run(credentials["email"], credentials["password"])
