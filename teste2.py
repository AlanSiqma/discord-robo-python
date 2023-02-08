# bot.py
import os
import random
from dotenv import load_dotenv
import discord
# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# 2
bot = commands.Bot(intents=intents, command_prefix='/')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    ctx.typing()
    # for member in ctx.guild.members:
    #     print("{},{}".format(member, member.id))

    brooklyn_99_quotes = [
        'I\'m the huaman form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.reply(response)


@bot.command(name='private_message', help="Robo's reply in private")
async def private_message(ctx):
    ctx.typing()
    await ctx.author.send("Mensagem em privado")


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    ctx.typing()
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.reply(', '.join(dice))

bot.run(TOKEN)
