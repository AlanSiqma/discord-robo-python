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

array = []


@bot.command(name='add_objectives', help="Robo's reply in private")
async def add_objectives(ctx, objectives):
    for objective in objectives.split(','):
        array.append(objective)

    ctx.typing()
    await ctx.reply("Objetivos adicionados")


@bot.command(name='list_objectives', help="Robo's reply in private")
async def list_objectives(ctx):
    ctx.typing()
    await ctx.reply(', '.join(array))


@bot.command(name='remove_objective', help="Robo's reply in private")
async def remove_objective(ctx, item):
    ctx.typing()
    array.remove(item)
    await ctx.reply("Item removido com sucesso")

bot.run(TOKEN)
