import os
import sys
import json
import datetime
import pymongo
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

with open("./config.json") as x:
    configData = json.load(x)

@bot.event
async def on_ready():
    # Prints to console telling us that it is logged in.
    print(f'Logged in as {bot.user}\n')
    # Status for the bot.
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="/story"))

bot.run(configData["TOKEN"])