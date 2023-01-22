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
        await QuestionPrompt.fourResponseQuestion(interaction, firstQuestion)
    
class questionDropdown(nextcord.ui.View):
    @nextcord.ui.select(
        placeholder='Choose a selection!',

        min_values=1,
        max_values=1,

        options = [

            nextcord.SelectOption(
                label = "1",
                value = "1"
            ),

            nextcord.SelectOption(
                label = "2",
                value = "2"
            ),

            nextcord.SelectOption(
                label = "3",
                value = "3"
            ),

            nextcord.SelectOption(
                label = "4",
                value = "4"
            ),
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        print(select.values[0])
