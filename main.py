import discord
from discord.commands import Option
import os
from dotenv import load_dotenv
from discord.commands import slash_command

load_dotenv('.env')
token = os.getenv('BOT_TOKEN')
guildId = os.getenv('GUILD_ID')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

status = discord.Status.online
activity = discord.Activity(type=discord.ActivityType.watching, name="Drachenlord")
bot = discord.Bot(
    intents = intents,
    status = status,
    activity = activity
    )
# debug_guilds = [guildId]

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        # if os.path.exists(os.path.join('modules', folder, 'cog.py')):
        #     bot.load_extension(f'modules.{folder}.cog')

@bot.event
async def on_ready():
    print(f"{bot.user} ist online")
    
# @bot.event   
# async def on_message(msg):
#     if msg.author.bot:
#         return
    
#     await msg.channel.send('jop')
    
# @bot.event
# async def on_message_delete(msg):
#     await msg.channel.send(f"Eine Nachricht von {msg.author} wurde gelöscht: '{msg.content}'")
    


bot.run(token)

