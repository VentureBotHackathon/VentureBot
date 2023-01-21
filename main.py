import os
import json
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

with open("./config.json") as x:
    configData = json.load(x)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}\n')
    await bot.change_presence(status=nextcord.Status.dnd, activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="/story"))

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

bot.run(configData["TOKEN"])