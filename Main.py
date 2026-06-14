import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user.name}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command()
async def server(ctx):
    await ctx.send(f'📊 Server Name: {ctx.guild.name}')

# Load token from environment variable
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
