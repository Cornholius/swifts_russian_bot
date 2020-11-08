from discord.ext import commands
from bot_token import TOKEN


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
