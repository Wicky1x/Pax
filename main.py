import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="/") # Will use slash commands later so...
for file in os.listdir("./cogs"):
    if filename.endswith(".py"):
       bot.load_extension(f"cogs.{filename[:-3]}")
bot.run("TOKEN")
