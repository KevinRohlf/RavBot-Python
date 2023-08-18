import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from dotenv import load_dotenv
import os




class Commands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command()
    async def activity(
        self, ctx,
        typ: Option(str, choices=["game", "stream", "watch"]),
        status: Option(str, choices=["online", "abwesend", "beschäftigt", "offline"]),
        name: Option(str)
    ):
        if typ == "game":
            act = discord.Game(name=name)
        elif typ == "stream":
            act = discord.Streaming(
                name=name,
                url="https://www.twitch.tv/ravalay"
                )
        elif typ == "watch":
            act = discord.Activity(
                type=discord.ActivityType.watching,
                name=name
                )
            
            
        if status == "online":
            stat = discord.Status.online
        elif status == "abwesend":
            stat = discord.Status.idle
        elif status == "beschäftigt":
            stat = discord.Status.do_not_disturb
        elif status == "offline":
            stat = discord.Status.invisible
        
        
        await self.bot.change_presence(activity=act, status=stat)
        await ctx.respond("Status wurde geändert", ephemeral=True)
    


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))