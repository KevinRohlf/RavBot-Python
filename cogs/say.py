import discord
from discord.commands import slash_command, Option
from discord.ext import commands


class Say(commands.Cog, name="say"):
    """Simple Command to greet your friends"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name = "say", description = "lässt den Bot eine Nachricht schreiben")
    async def say(self, ctx, text: Option(str, "schreibe hier die Nachricht"), channel: Option(discord.TextChannel)):
        await channel.send(text)
        await ctx.respond("Die Nachricht wurde gesendet", ephemeral=True)
        


def setup(bot: commands.Bot):
    bot.add_cog(Say(bot))