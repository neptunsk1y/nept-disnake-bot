import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready!")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(os.getenv('TOKEN'))