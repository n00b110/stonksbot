import discord
import yfinance as yf
from discord.ext import commands
from re import match
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def check(ctx, arg):
    stock_info = yf.Ticker(arg).info
    stock_price = stock_info["regularMarketPrice"]
    await ctx.send(stock_price)
    

bot.run(token)

