import nextcord
from nextcord.utils import get
from nextcord import Interaction
from nextcord.ext import commands

class QuestionPrompt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    async def fourResponseQuestion(self, prompt):
        msg = await self.send(prompt)
        full_msg = await msg.fetch(msg)
        await full_msg.add_reaction('🤖')
        reaction = get(full_msg.reactions, emoji='🤖')
        COUNT = reaction.count
        print(COUNT)