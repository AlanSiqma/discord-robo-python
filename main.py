
import os
from DAO import objective_repository
from dotenv import load_dotenv
import discord

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix='/')


@bot.event
async def on_ready():
    print(f'{bot.user.name} o robo está conectado no Discord!')


@bot.command(name='add_objectives', help="Adicionando um novo objetivo para o usuario")
async def add_objectives(ctx, objectives):
    array = []
    ctx.typing()

    for objective in objectives.split(','):
        array.append(objective)

    objective_repository.add_objective_json(ctx.author.id, array)

    await ctx.reply("Objetivos adicionados")


@bot.command(name='list_objectives', help="Listando os objetivos do usuario")
async def list_objectives(ctx):
    ctx.typing()

    data = objective_repository.get_single_objective(ctx.author.id)

    await ctx.reply(', '.join(data['array']))


@bot.command(name='remove_objective', help="Deletando um objetivo do usuario")
async def remove_objective(ctx, item):
    ctx.typing()

    objective_repository.remove_objective(ctx.author.id, item)

    await ctx.reply("Item removido com sucesso")


bot.run(TOKEN)
