import random
import nextcord
import time
from nextcord.utils import get
from nextcord import Interaction
from nextcord.ext import commands
from database.database import Database

class QuestionPrompt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    async def fourResponseQuestion(interaction):
        prompt = Database.promptArray[1]
        message = await interaction.send(prompt, view=questionDropdown(timeout=None))

    async def survivedTrip(interaction):
        prompt = Database.promptArray[5]
        await interaction.send(prompt, view=surviveQuestionDropdown(timeout=None))

    async def stickers(interaction):
        prompt = Database.promptArray[8]
        await interaction.send(prompt, view=stickerQuestionDropdown(timeout=None))

    async def whereTo(interaction):
        prompt = Database.promptArray[11]
        await interaction.send(prompt,view=whereQuestionDropdown(timeout=None))
    

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
        if (select.values[0] != "D"):
            await QuestionPrompt.survivedTrip(interaction)
        elif (select.values[0] == "D"):
            await interaction.send(Database.promptArray[2])
            coinflip = random.choice([0,1]) 
            if coinflip == 1:
                await interaction.send(Database.promptArray[4])
                QuestionPrompt.survivedTrip(interaction)
            else:
                await interaction.send(Database.promptArray[3])

            

class surviveQuestionDropdown(nextcord.ui.View):
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
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        if (select.values[0] == "A"):
            await interaction.send(Database.promptArray[6])
            QuestionPrompt.stickers(interaction)
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[3])

class stickerQuestionDropdown(nextcord.ui.View):
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
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        if (select.values[0] == "B"):
            await interaction.send(Database.promptArray[10])
            QuestionPrompt.whereTo(interaction)
        elif (select.values[0] == "A"):
            await interaction.send(Database.promptArray[9])


class whereQuestionDropdown(nextcord.ui.View):
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
        if (select.values[0] == ""):
            await interaction.send(Database.promptArray[6])
            QuestionPrompt.whereTo(interaction)
        elif (select.values[0] == "A"):
            await interaction.send(Database.promptArray[3])