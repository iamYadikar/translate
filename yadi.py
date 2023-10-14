import discord
import random
from discord.ext import commands

intents = discord.Intents.default() # Переменная intents - хранит привилегии бота
intents.message_content = True # Включаем привелегию на чтение сообщений


bot = commands.Bot(command_prefix='$', intents=intents) # Создаем бота в переменной client и передаем все привелегии


def generator_pass(pass_length = 10):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def password(ctx):
    await ctx.send(generator_pass())

bot.run('token')
    
