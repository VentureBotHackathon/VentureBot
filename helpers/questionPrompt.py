import random
import nextcord
import time
from nextcord.utils import get
from nextcord import Interaction
from nextcord.ext import commands
from database.database import Database
score = 0
class QuestionPrompt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def fourResponseQuestion(interaction):
        prompt =  Database.imgArray[19] + '\n' + Database.promptArray[1]
        message = await interaction.send(prompt, view=questionDropdown(timeout=None))

    async def survivedTrip(interaction):
        prompt = Database.imgArray[7] + '\n' + Database.promptArray[5]
        await interaction.send(prompt, view=entranceQuestionDropdown(timeout=None))

    async def stickers(interaction):
        prompt = Database.imgArray[3] + '\n' + Database.promptArray[8]
        await interaction.send(prompt, view=stickerQuestionDropdown(timeout=None))

    async def whereTo(interaction):
        prompt = Database.promptArray[11]
        await interaction.send(prompt,view=whereQuestionDropdown(timeout=None))
    
    async def team(interaction):
        prompt = Database.promptArray[17]
        await interaction.send(prompt,view=teamQuestionDropdown(timeout=None))

    async def clown(interaction):
        prompt = Database.imgArray[14] + "\n" + Database.promptArray[13]
        await interaction.send(prompt,view=clownQuestionDropdown(timeout=None))

    async def single(interaction):
        prompt = Database.imgArray[15] + "\n" + Database.promptArray[18]
        await interaction.send(prompt,view=singleQuestionDropdown(timeout=None))

    async def hoodie(interaction):
        prompt = Database.promptArray[22]
        await interaction.send(prompt,view=hoodieQuestionDropdown(timeout=None))

    async def opening(interaction):
        prompt = Database.promptArray[25]
        await interaction.send(prompt,view=openingQuestionDropdown(timeout=None))

    async def lunch(interaction):
        prompt = Database.imgArray[4] + "\n" + Database.promptArray[29]
        await interaction.send(prompt,view=lunchQuestionDropdown(timeout=None))

    async def redbull(interaction):
        prompt = Database.promptArray[33]
        await interaction.send(prompt,view=redbullQuestionDropdown(timeout=None))

    async def dinner(interaction):
        prompt = Database.imgArray[20] + "\n" + Database.promptArray[36]
        await interaction.send(prompt,view=dinnerQuestionDropdown(timeout=None))

    async def debug(interaction):
        prompt = Database.promptArray[39]
        await interaction.send(prompt,view=debugQuestionDropdown(timeout=None))

    async def money(interaction):
        prompt = Database.promptArray[42]
        await interaction.send(prompt,view=moneyQuestionDropdown(timeout=None))


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
        global score
        time.sleep(2)
        if (select.values[0] != "D"):
            await QuestionPrompt.survivedTrip(interaction)
            score += 100
        elif (select.values[0] == "D"):
            await interaction.send(Database.promptArray[2])
            time.sleep(2)
            coinflip = random.choice([0,1]) 
            if coinflip == 1:
                await interaction.send(Database.imgArray[12] + "\n" + Database.promptArray[4])
                time.sleep(2)
                await QuestionPrompt.survivedTrip(interaction)
                score += 200
            elif coinflip == 0:
                await interaction.send(Database.promptArray[3])
                time.sleep(2)
                await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + str(score))

            

class entranceQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.imgArray[8] + "\n" + Database.promptArray[6])
            time.sleep(2)
            await QuestionPrompt.stickers(interaction)
            score += 100
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[7])
            time.sleep(2)
            await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + str(score))

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
        global score
        time.sleep(2)
        if (select.values[0] == "B"):
            await interaction.send(Database.imgArray[16] + "\n" + Database.promptArray[10])
            time.sleep(2)
            await QuestionPrompt.whereTo(interaction)
            score -= 100
        elif (select.values[0] == "A"):
            await interaction.send(Database.promptArray[9])
            time.sleep(2)
            await QuestionPrompt.whereTo(interaction)
            score += 100


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
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.imgArray[2] + "\n" + Database.promptArray[12])
            time.sleep(2)
            await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + score)
        elif (select.values[0] == "B"):
            await interaction.send(Database.imgArray[6] + "\n" + Database.promptArray[16])
            time.sleep(2)
            await QuestionPrompt.team(interaction)
            score += 100
        elif (select.values[0] == "C"):
            await QuestionPrompt.clown(interaction)

        


class clownQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "B"):
            await interaction.send(Database.promptArray[15])
            time.sleep(2)
            await interaction.send(Database.promptArray[16])
            time.sleep(2)
            await QuestionPrompt.team(interaction)
            score += 100
        elif (select.values[0] == "A"):
            await interaction.send(Database.promptArray[14])
            time.sleep(2)
            await interaction.send(Database.promptArray[16])
            time.sleep(2)
            await QuestionPrompt.team(interaction)
            score -= 100


class teamQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.promptArray[21])
            time.sleep(2)
            await QuestionPrompt.hoodie(interaction)
            score += 100
        elif (select.values[0] == "B"):
            await QuestionPrompt.single(interaction)



class singleQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.promptArray[19])
            time.sleep(2)
            await interaction.send(Database.promptArray[21])
            time.sleep(2)
            await QuestionPrompt.hoodie(interaction)
            score += 200
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[20])
            time.sleep(2)
            await interaction.send(Database.promptArray[21])
            time.sleep(2)
            await QuestionPrompt.hoodie(interaction)
            score -= 100


class hoodieQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.imgArray[16] + "\n" + Database.promptArray[23])
            time.sleep(2)
            await QuestionPrompt.opening(interaction)
            score -= 100
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[24])
            time.sleep(2)
            await QuestionPrompt.opening(interaction)
            score += 100


class openingQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.imgArray[17] + "\n" + Database.promptArray[26])
            time.sleep(2)
            await interaction.send(Database.promptArray[28])
            time.sleep(2)
            await QuestionPrompt.lunch(interaction)
            score -= 100
        elif (select.values[0] == "B"):
            await interaction.send(Database.imgArray[18] + "\n" + Database.promptArray[27])
            time.sleep(2)
            await interaction.send(Database.promptArray[28])
            time.sleep(2)
            await QuestionPrompt.lunch(interaction)
            score += 100


class lunchQuestionDropdown(nextcord.ui.View):
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
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.promptArray[30])
            time.sleep(2)
            await QuestionPrompt.redbull(interaction)
            score -= 100
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[31])
            time.sleep(2)
            await QuestionPrompt.redbull(interaction)
            score += 100
        elif (select.values[0] == "C"):
            await interaction.send(Database.promptArray[32])
            time.sleep(2)
            await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + str(score))


class redbullQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.imgArray[9] + "\n" + Database.promptArray[34])
            time.sleep(2)
            await QuestionPrompt.dinner(interaction)
            score += 100
        elif (select.values[0] == "B"):
            await interaction.send(Database.imgArray[10] + "\n" + Database.promptArray[35])
            time.sleep(2)
            await QuestionPrompt.dinner(interaction)
            score -= 100
            


class dinnerQuestionDropdown(nextcord.ui.View):
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
        ]
    )

    async def callback(self, select, interaction: nextcord.Interaction):
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.promptArray[37])
            time.sleep(2)
            await QuestionPrompt.debug(interaction)
            score += 200
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[38])
            time.sleep(2)
            await QuestionPrompt.debug(interaction)
            score += 100
        elif (select.values[0] == "C"):
            await interaction.send(Database.promptArray[32])
            time.sleep(2)
            await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + str(score))


class debugQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] == "A"):
            await interaction.send(Database.imgArray[21] + "\n" + Database.promptArray[40])
            time.sleep(2)
            await QuestionPrompt.money(interaction)
            score += 100
        elif (select.values[0] == "B"):
            await interaction.send(Database.promptArray[41])
            time.sleep(2)
            await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + str(score))
        

class moneyQuestionDropdown(nextcord.ui.View):
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
        global score
        time.sleep(2)
        if (select.values[0] != "D"):
            await interaction.send(Database.imgArray[22] + "\n" + Database.promptArray[43])
            time.sleep(2)
            score += 100
            await interaction.send("Your final score was: " + str(score))
        elif (select.values[0] == "D"):
            await interaction.send(Database.imgArray[23] + "\n" + Database.promptArray[44])
            time.sleep(2)
            await interaction.send(Database.imgArray[13] + "\n" + "Your final score was: " + str(score))


