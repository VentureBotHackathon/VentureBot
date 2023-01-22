import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from storymodes.nwhacks import Nwhacks
from helpers.questionPrompt import QuestionPrompt
from database.database import Database

class Story(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Begin a new story and start voting")
    async def story(self, interaction: Interaction):
        await interaction.send(Database.imgArray[1] + '\n' + "Message", view=StoryDropdown(timeout=None))

class StoryDropdown(nextcord.ui.View):
    @nextcord.ui.select(
        placeholder='Please choose a story',

        min_values=1,
        max_values=1,

        options =[

            nextcord.SelectOption(
                label = "NWHacks 2023",
                emoji = "🔌",
                description = "Explore the hackathon and become a winner!",
                value='nwhacks'
            ),

            nextcord.SelectOption(
                label = "Story #2",
                emoji = "⚙️",
                description = "2nd Story to be added",
                value='story2'
            )
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        if (select.values[0] == "nwhacks"):
            await QuestionPrompt.fourResponseQuestion(interaction)

        elif (select.values[0] == "story2"):
            await interaction.send("You choosed story2")

def setup(bot):
    bot.add_cog(Story(bot))