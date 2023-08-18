import discord
from discord.commands import slash_command, Option
from discord.ext import commands


class Info(commands.Cog, name="Info"):
    """Simple Command to greet your friends"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name = "info", description = "info über einen User")
    async def info(
        self,
        ctx,
        alter: Option(int, "Das Alter", min_value=1, max_value=105),
        user: Option(discord.Member, "gib einen User an", default=None)
    ):
        if user is None:
            user = ctx.author
            
        embed = discord.Embed(
            title=f"Infos über {user.name}",
            description=f"Hier die Infos über {user.mention}",
            color= discord.Color.random()
        )
        
        time = discord.utils.format_dt(user.created_at, "R")
        
        embed.add_field(name="Account erstellt ", value=time, inline=False)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Alter", value=alter)
        
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text="Stalker")
        
        await ctx.respond(embed=embed)
        
        


def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))