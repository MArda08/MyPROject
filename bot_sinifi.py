import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
@bot.command()
async def hi(ctx):
    await ctx.send(f'bye')
@bot.command()
async def parola(ctx):
    await ctx.send(f'gen_pass(12)')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("GİZLİ TOKEN BURAYA")
