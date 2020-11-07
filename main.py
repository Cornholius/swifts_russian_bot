import discord
from discord.ext import commands
from bot_token import TOKEN

# <RawReactionActionEvent message_id=774201412581982219 user_id=285056432808919040 channel_id=486609181424746499 guild_id=486609181424746497 emoji=<PartialEmoji animated=False name='pidori' id=712304327808778290> event_type='REACTION_ADD' member=<Member id=285056432808919040 name='Corn' discriminator='2313' bot=False nick=None guild=<Guild id=486609181424746497 name='Хижина краболова' shard_id=None chunked=False member_count=7>>>

bot = commands.Bot(command_prefix='!')

cogs = ['plugins.info',
        'plugins.minerals',
        'plugins.requests'
        ]
for cog in cogs:
    bot.load_extension(cog)
    print('Loading ', cog)


@bot.event
async def on_ready():
    print('Bot started')

bot.run(TOKEN)


# import discord
# from discord import utils
#
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_raw_reaction_add(self, payload):
#         print(payload)
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