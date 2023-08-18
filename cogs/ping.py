import discord
from discord.commands import slash_command
from discord.ext import commands


class Ping(commands.Cog, name="Ping"):
    """Simple ping command to test responses and permissions of the bot"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name='ping', description='ping')
    async def annonew(self,  ctx: commands.Context):
        """the bot responds to this command "pong" if the user has the "bot_commander" role"""
        await ctx.respond(f'{ctx.author.mention}\nPong! {round(self.bot.latency * 1000)}ms')


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))