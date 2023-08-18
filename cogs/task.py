import discord
from discord.commands import slash_command
from discord.ext import commands, tasks
from datetime import time, timezone


class Task(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.time_task.start()
        
    
    # @tasks.loop(seconds=5)
    # async def rava(self):
    #     if self.rava.current_loop == 0:
    #         return
    #     print("rava")
        
    @tasks.loop(
        time=time(22, 10, tzinfo=timezone.utc)
    )
    async def time_task(self):
        print("Uhrzeit")
    


def setup(bot: commands.Bot):
    bot.add_cog(Task(bot))