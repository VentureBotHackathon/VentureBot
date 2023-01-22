import os
import json
import datetime
import pytz
from pymongo import MongoClient
from nextcord.ext import commands

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    with open("./config.json") as x:
        configData = json.load(x)

    cluster = MongoClient(configData["DATABASEPASSWORD"])
    db = cluster["VentureBot"]
    prompts = db["Prompts"]

    array = []
    count = 1
    array.append("Nothing")

    for x in prompts.find():
        collection = "Prompt" + str(count)
        array.append(x[collection])
        count += 1

    print(array[1])

    print(array[5])


