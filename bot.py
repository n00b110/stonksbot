import discord
import pendulum
import yfinance as yf
from discord.ext import commands
import pandas_datareader.data as web
import matplotlib.pyplot as plot
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
    await ctx.send(f"{arg} - {stock_price}")
    

@bot.command()
async def chart(ctx, ticker1):
    data = web.DataReader(name="TSLA", data_source="yahoo", start="2021-09-11", end="2022-09-11")
    close = data['Close']
    axis = close.plot()
    axis.set_xlabel('Close')
    axis.set_ylabel('Date')
    axis.grid()
    plot.savefig("TSLA.png")
    await ctx.channel.send(file=discord.File("TSLA.png"))



bot.run(token)

