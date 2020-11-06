import discord
from discord.ext import commands
from bot_token import TOKEN

bot = commands.Bot(command_prefix='!')
client = discord.Client()

cogs = ['plugins.info',
        'plugins.minerals',
        'plugins.requests',
        'plugins.test'
        ]
for cog in cogs:
    bot.load_extension(cog)
    print('Loading ', cog)


@bot.event
async def on_ready():
    print('Bot started')

bot.run(TOKEN)
# client.run(TOKEN)
# import discord
# from discord import utils
#
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_raw_reaction_add(self, payload):
#         print(payload.message_id)
#         if payload.message_id == 774201412581982219:
#             print(payload.message_id)
#             channel = self.get_channel(payload.channel_id)  # получаем объект канала
#             print(channel)
#             message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
#             print(message.content)
#             member = utils.get(message.guild.members,
#                                id=payload.user_id)  # получаем объект пользователя который поставил реакцию
#             print(member.name)
#
# client = MyClient()
# client.run(TOKEN)