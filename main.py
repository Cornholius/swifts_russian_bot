import discord
import random
from discord.ext import commands
from minerals import all_items, all_id
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
color_list = [i[0] for i in cursor.execute("SELECT value FROM colors").fetchall()]
bot = commands.Bot(command_prefix='!')
client = discord.Client()

cogs = ['info']


@bot.event
async def on_ready():
    print('Bot started')
    for cog in cogs:
        bot.load_extension(cog)

@bot.command(pass_context=True, name='минералы')
async def minerals1(ctx):
    msg = await ctx.send(content='Щас чекнем твоё говно...')
    buy = all_items()[0]
    sell = all_items()[1]
    embed = discord.Embed(title='Твои сраные миники',
                          color=random.choice(color_list))
    embed.add_field(name='Items', value="Tritanium\n Pyerite\n Mexallon\n Isogen\n Nocxium\n"
                                        "Zydrine\n Megacyte\n Morphite", inline=True)
    embed.add_field(name='Sell',
                    value="{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n".format(
                        sell['Tritanium'], sell['Pyerite'], sell['Mexallon'], sell['Isogen'],
                        sell['Nocxium'], sell['Zydrine'], sell['Megacyte'], sell['Morphite']), inline=True)
    embed.add_field(name='Buy',
                    value="{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n".format(
                        buy['Tritanium'], buy['Pyerite'], buy['Mexallon'], buy['Isogen'],
                        buy['Nocxium'], buy['Zydrine'], buy['Megacyte'], buy['Morphite']), inline=True)
    await msg.edit(embed=embed, content=None)


@bot.command(pass_context=True, name='миники')
async def minerals2(ctx):
    msg = await ctx.send(content='Щас чекнем твоё говно...')
    buy = all_items()[0]
    sell = all_items()[1]
    embed = discord.Embed(title='Твои сраные миники', color=random.choice(color_list))
    for key in all_id:
        embed.add_field(name=key, value='Sell: {} // Buy: {}'.format(sell[key], buy[key]), inline=False)
    await msg.edit(embed=embed, content=None)


@bot.command(pass_context=True, name='qwe')
async def qwe(ctx):
    embed = discord.Embed(title='654645 654654 54654')
    embed.add_field(name='eweqewqe', value='3232323', inline=True)
    embed.add_field(name='eweqewqe', value='3232323', inline=True)
    await ctx.send(embed=embed)

# @bot.event
# async def on_message(message):
#     print('{0.id} {0.author}: {0.content}'.format(message))

bot.run(cursor.execute("SELECT value FROM token").fetchone()[0])
