import json
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
    images = db["Images"]

    promptArray = []
    count = 1
    promptArray.append("Nothing")

    for x in prompts.find():
        collection = "Prompt" + str(count)
        promptArray.append(x[collection])
        count += 1
    
    
