import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from helpers.questionPrompt import QuestionPrompt

class Nwhacks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def questionList(interaction):
        firstQuestion = "test"
        await QuestionPrompt.fourResponseQuestion(interaction, firstQuestion)
