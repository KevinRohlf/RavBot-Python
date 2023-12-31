import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv("../.env")

welcomeId = os.getenv('WELCOMECHANNEL_ID')




class Greeting(commands.Cog, name="Greeting"):
    """Simple Command to greet your friends"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name = "greeting", description = "Grüße einen User")
    async def greet(self, ctx, user: Option(discord.Member, "Der User den du grüßen möchtest")):
        await ctx.respond(f"Hallo {user.mention}")
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Willkommen",
            description=f"Moin Servus Moin {member.mention}",
            color= discord.Color.random()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        
        channel = await self.bot.fetch_channel(welcomeId)
        await channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Greeting(bot))