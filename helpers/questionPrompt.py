import nextcord
import time
from nextcord.utils import get
from nextcord import Interaction
from nextcord.ext import commands

class QuestionPrompt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    async def fourResponseQuestion(interaction, prompt):
        message = await interaction.send(prompt, view=questionDropdown(timeout=None))

class questionDropdown(nextcord.ui.View):
    @nextcord.ui.select(
        placeholder='Choose a selection!',

        min_values=1,
        max_values=1,

        options = [

            nextcord.SelectOption(
                label = "A",
                value = "A"
            ),

            nextcord.SelectOption(
                label = "B",
                value = "B"
            ),

            nextcord.SelectOption(
                label = "C",
                value = "C"
            ),

            nextcord.SelectOption(
                label = "D",
                value = "D"
            ),
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        return(select.values[0])
 