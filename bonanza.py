import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

muz_puani = 0
carpan = random.randint(1,10)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')

@bot.command()
async def hello(ctx):
    await ctx.send("Merhaba")

@bot.command()
async def kredi(ctx):
    await ctx.send(muz_puani)


@bot.command(name='muz', help='Rastgele bir sayıyı çarparak Muz Puanınızı arttırır.')
async def muz(ctx):
    global muz_puani
    global carpan

    random_sayi = random.randint(1, 500)
    katlanan_sayi = round(random_sayi * carpan)

    muz_puani += katlanan_sayi

    await ctx.send(f'Rastgele sayı: {random_sayi}\nÇarpan: {carpan}\nKatlanan Sayı: {katlanan_sayi}\nMuz Puanınız: {muz_puani}')

bot.run("MTE5NjQ5MzgxOTgzMTY1NjQ3OA.G_1gaC.H-0D2gf3OQawu-ZrVwFDdgP5XWNdMyNjlmL3Ns")
