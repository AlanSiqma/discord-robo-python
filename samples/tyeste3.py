import discord
from dotenv import load_dotenv
import os

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == "?regras":
            await message.channel.send(f'as regras do servior são:{os.linesep}1- tem que ser engenheiro{os.linesep}2- so pode ser engenheiro')
        elif message.content == "?nivel":
            await message.author.send(f'Nível 1')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)

client.run(os.getenv('TOKEN'))
