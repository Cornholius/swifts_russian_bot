import discord
from discord.ext import commands
import sqlite3
from bot_token import TOKEN

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
color_list = [i[0] for i in cursor.execute("SELECT value FROM colors").fetchall()]
bot = commands.Bot(command_prefix='!')
client = discord.Client()

cogs = ['plugins.info', 'plugins.minerals', 'plugins.requests']
for cog in cogs:
    bot.load_extension(cog)
    print('Loading ', cog)

@bot.event
async def on_ready():
    print('Bot started')


# @commands.command(pass_context=True, name='qwe')
# async def qwe(ctx):
#     embed = discord.Embed(title='654645 654654 54654')
#     embed.add_field(name='eweqewqe', value='3232323', inline=True)
#     embed.add_field(name='eweqewqe', value='3232323', inline=True)
#     await ctx.send(embed=embed)


# @bot.event
# async def on_message(message):
#     print('{0.id} {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
