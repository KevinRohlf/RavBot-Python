import discord
from discord.commands import slash_command, Option
from discord.ext import commands
from dotenv import load_dotenv
import os




class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(description="Kicke einen Member")
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def kick(self, ctx, member: Option(discord.Member, "Wähle ein Member")):
        try:
            await member.kick()
        except (discord.Forbidden, discord.HTTPException) as e:
            print(e)
            await ctx.respond("Ich habe keine Berechtigung, um diesen Member zu kicken")
            return
        await ctx.respond(f"{member.mention} wurde gekickt!")
        
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        await ctx.respond(f"Es ist ein fehler aufgetreten: ```{error}```")
        raise error
    

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))