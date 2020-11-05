import discord
from discord.ext import commands
from bot_token import TOKEN

bot = commands.Bot(command_prefix='!')
client = discord.Client()

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


# @bot.event
# async def on_message(message):
#     print('{0.id} {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
