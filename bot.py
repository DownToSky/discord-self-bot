import discord
from discord.ext import commands
import json

description = "```A self bot with a lot of utility commands and functionality. Mainly trying to not attract attetion of your fellow chatters```"

credentials = {"email" : "",
        "password" : "",
        }

#WARNING: this needs to use OS.PATH!
def get_credentials():
    with open("cred/email.txt", 'r') as email_f:
        #Get the email with regualar expressions
    with open("cred/pass.txt", 'r') as password_f:
        #Get the password with regular expressions

bot = commands.Bot(command_prefix = '@', description = description)


@bot.event
async def on_read():
    user_name = bot.user.name.encode("utf8")
    print("Logged in as")
    print(user_name)
    print(bot.user.id)

bot.run(credentials["email"], credentials["password"])
