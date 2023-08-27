import discord
from discord.commands import slash_command, Option
from discord.ext import commands





class Button(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(View())

    @slash_command()
    async def button1(self, ctx):
        await ctx.respond("Klicke hier!", view=View())
    

def setup(bot: commands.Bot):
    bot.add_cog(Button(bot))
    
    
class View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Button 1", style=discord.ButtonStyle.primary, custom_id="button1")
    async def button_callback1(self, button, interaction):
        button1 = [x for x in self.children if x.custom_id=="button2"][0]
        
        if button1.disabled == True:
            button1.disabled = False
            await interaction.response.send_message("Button 2 ist wieder klickbar", ephemeral=True)
            
        else:
            await interaction.response.send_message("Hey!", ephemeral=True)
        
        button.disabled = True
        await interaction.message.edit(view=self)
        
        
        
    @discord.ui.button(label="Button 2", style=discord.ButtonStyle.primary, custom_id="button2")
    async def button_callback2(self, button, interaction):
        button.disabled = True
        button1 = [x for x in self.children if x.custom_id=="button1"][0]
        if button1.disabled == True:
            button1.disabled = False
            await interaction.response.send_message("Button 1 ist wieder klickbar", ephemeral=True)
            
        else:
            await interaction.response.send_message("Hey!", ephemeral=True)
        
        button.disabled = True
        await interaction.message.edit(view=View2())
        
        # await interaction.message.edit(view=self) # kann man öfters machen ist aber keine gültige antwort und funktioniert nicht bei unsichtbaren nachrichten
        # await interaction.response.edit_message(view=self) #kann man nur einmal machen und ist eine gültige antwort (muss einmal drinne sein)
        
        
class View2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Button 3", style=discord.ButtonStyle.primary, custom_id="button3", emoji="😂")
    async def button_callback3(self, button, interaction):
        button1 = [x for x in self.children if x.custom_id=="button4"][0]
        
        if button1.disabled == True:
            button1.disabled = False
            await interaction.response.send_message("Button 2 ist wieder klickbar", ephemeral=True)
            
        else:
            await interaction.response.send_message("Hey!", ephemeral=True)
        
        button.disabled = True
        await interaction.message.edit(view=self)
        
        
        
    @discord.ui.button(label="Button 4", style=discord.ButtonStyle.primary, custom_id="button4")
    async def button_callback4(self, button, interaction):
        button.disabled = True
        button1 = [x for x in self.children if x.custom_id=="button3"][0]
        if button1.disabled == True:
            button1.disabled = False
            await interaction.response.send_message("Button 1 ist wieder klickbar", ephemeral=True)
            
        else:
            await interaction.response.send_message("Hey!", ephemeral=True)
        
        button.disabled = True
        await interaction.message.edit(view=self)