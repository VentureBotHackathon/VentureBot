import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from helpers.questionPrompt import QuestionPrompt
from database.database import Database

class Nwhacks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    bot = commands.Bot(command_prefix='$')

    async def questionList(interaction):
        firstQuestion = Database.promptArray[1]
        response = await QuestionPrompt.fourResponseQuestion(interaction, firstQuestion)

    async def didNotMakeIt(interaction):
        firstQuestion = Database.promptArray[3]
        await QuestionPrompt.fourResponseQuestion(interaction, firstQuestion)

    async def frontEntrance(interaction):
        firstQuestion = Database.promptArray[4]
        response = await QuestionPrompt.fourResponseQuestion(interaction, firstQuestion)
    


