import json
from pymongo import MongoClient
from nextcord.ext import commands
from bson.objectid import ObjectId

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
    
    imgArray=[]
    imgArray.append("None")
    x1 = images.find_one({"_id": ObjectId('63cc841c23e82bdef00c9f76')})
    imgArray.append(x1["nwhacks"])

    x2 = images.find_one({"_id": ObjectId('63cc845323e82bdef00c9f77')})
    imgArray.append(x2["snacks"])
    
    x3 = images.find_one({"_id": ObjectId('63cc84cf23e82bdef00c9f78')})
    imgArray.append(x3["stickerswag"])

    x4 = images.find_one({"_id": ObjectId('63cc84e623e82bdef00c9f79')})
    imgArray.append(x4["banhmi"])

    x5 = images.find_one({"_id": ObjectId('63cc84ff23e82bdef00c9f7a')})
    imgArray.append(x5["vendingmachine"])

    x6 = images.find_one({"_id": ObjectId('63cc851423e82bdef00c9f7b')})
    imgArray.append(x6["atrium"])

    x7 = images.find_one({"_id": ObjectId('63cc852323e82bdef00c9f7c')})
    imgArray.append(x7["healthsciences"])

    x8 = images.find_one({"_id": ObjectId('63cc853323e82bdef00c9f7d')})
    imgArray.append(x8["reception"])

    x9 = images.find_one({"_id": ObjectId('63cc854223e82bdef00c9f7e')})
    imgArray.append(x9["angrymonkey"])

    x10 = images.find_one({"_id": ObjectId('63cc855223e82bdef00c9f7f')})
    imgArray.append(x10["typemonkey"])
    
    x11 = images.find_one({"_id": ObjectId('63cc856223e82bdef00c9f80')})
    imgArray.append(x11["agronomyroad"])

    x12 = images.find_one({"_id": ObjectId('63cc85c423e82bdef00c9f85')})
    imgArray.append(x12["cool"])

    x13 = images.find_one({"_id": ObjectId('63cc85ce23e82bdef00c9f86')})
    imgArray.append(x13["gameover"])

    x14 = images.find_one({"_id": ObjectId('63cc85d923e82bdef00c9f87')})
    imgArray.append(x14["clown"])

    x15 = images.find_one({"_id": ObjectId('63cc85e223e82bdef00c9f88')})
    imgArray.append(x15["girl"])

    x16 = images.find_one({"_id": ObjectId('63cc85ec23e82bdef00c9f89')})
    imgArray.append(x16["disappointed"])

    x17 = images.find_one({"_id": ObjectId('63cc85f523e82bdef00c9f8a')})
    imgArray.append(x17["rain"])

    x18 = images.find_one({"_id": ObjectId('63cc860123e82bdef00c9f8b')})
    imgArray.append(x18["nervous"])

    x19 = images.find_one({"_id": ObjectId('63cc953d23e82bdef00c9f8c')})
    imgArray.append(x19["transport"])

    x20 = images.find_one({"_id": ObjectId('63ccc5e723e82bdef00c9f95')})
    imgArray.append(x20["bowl"])

    x21 = images.find_one({"_id": ObjectId('63ccc60423e82bdef00c9f96')})
    imgArray.append(x21["happy"])

    x22 = images.find_one({"_id": ObjectId('63ccc93523e82bdef00c9f9b')})
    imgArray.append(x22["rich"])

    x23 = images.find_one({"_id": ObjectId('63ccc97423e82bdef00c9f9c')})
    imgArray.append(x23["robbed"])