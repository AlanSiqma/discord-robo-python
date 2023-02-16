# bot.py
import os
import json
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
    ctx.typing()

    for objective in objectives.split(','):
        array.append(objective)

    add_objective_json(ctx.author.id, array)

    await ctx.reply("Objetivos adicionados")


@bot.command(name='list_objectives', help="Robo's reply in private")
async def list_objectives(ctx):
    ctx.typing()
    data = get_single_objective(ctx.author.id)
    print(data)
    await ctx.reply(', '.join(data['array']))


@bot.command(name='remove_objective', help="Robo's reply in private")
async def remove_objective(ctx, item):
    ctx.typing()
    array.remove(item)
    await ctx.reply("Item removido com sucesso")


FILEPATH = 'teste.json'


def get_json_data():
    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    return data


def store_json_data(data):
    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)


def add_objective_json(id, array):

    current_data = {
        "id": id,
        "array": array
    }
    data = get_json_data()
    data.update(current_data)
    store_json_data(data)


def get_single_objective(id):
    data = get_json_data()
    print(data)
    if (id in data):
        return data[id]
    return None


def update_single_objective(id, array):
    data = get_json_data()
    if (id in data):
        current_data = {
            "id": id,
            "array": array
        }
    data[id] = current_data
    store_json_data(data)


bot.run(TOKEN)
