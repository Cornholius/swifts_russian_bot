import discord
import random
from discord.ext import commands
from minerals import all_items
from config import TOKEN, color_list
bot = commands.Bot(command_prefix='!')
client = discord.Client()
print('Bot started')


@bot.command(pass_context=True, name='минералы')
async def minerals1(ctx):
    msg = await ctx.send(content='Щас чекнем твоё говно...')
    buy = all_items()[0]
    sell = all_items()[1]
    embed = discord.Embed(title='Твои сраные миники',
                          color=random.choice(color_list))
    embed.add_field(name='Items', value="Tritanium\n Pyerite\n Mexallon\n Isogen\n Nocxium\n"
                                        "Zydrine\n Megacyte\n Morphite", inline=True)
    embed.add_field(name='Sell orders',
                    value="{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n".format(
                        sell['Tritanium'], sell['Pyerite'], sell['Mexallon'], sell['Isogen'],
                        sell['Nocxium'], sell['Zydrine'], sell['Megacyte'], sell['Morphite']), inline=True)
    embed.add_field(name='Buy orders',
                    value="{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n".format(
                        buy['Tritanium'], buy['Pyerite'], buy['Mexallon'], buy['Isogen'],
                        buy['Nocxium'], buy['Zydrine'], buy['Megacyte'], buy['Morphite']), inline=True)
    await msg.edit(embed=embed, content=None)


@bot.command(pass_context=True, name='миники')
async def minerals2(ctx):
    msg = await ctx.send(content='Щас чекнем твоё говно...')
    buy = all_items()[0]
    sell = all_items()[1]
    text = 'Tritanium s{} b{}\n Pyerite s{} b{}\n Mexallon s{} b{}\n Isogen s{} b{}\n Nocxium s{} b{}\n' \
           'Zydrine s{} b{}\n Megacyte s{} b{}\n Morphite s{} b{}'.format(sell['Tritanium'], buy['Tritanium'],
                                                                          sell['Pyerite'],buy['Pyerite'],
                                                                          sell['Mexallon'], buy['Mexallon'],
                                                                          sell['Isogen'], buy['Isogen'],
                                                                          sell['Nocxium'], buy['Nocxium'],
                                                                          sell['Zydrine'], buy['Zydrine'],
                                                                          sell['Megacyte'], buy['Megacyte'],
                                                                          sell['Morphite'], buy['Morphite'])
    embed = discord.Embed(title='Твои сраные миники',
                          description="".join(map(str, text)),
                          color=random.choice(color_list))
    await msg.edit(embed=embed, content=None)


@bot.command(pass_context=True, name='инфо')
async def info(ctx):
    embed = discord.Embed(title='Тебе, кожаный мешок, разрешается узнать:', color=random.choice(color_list))
    embed.add_field(name='!минералы',
                    value='Узнать курс миников в жите. Читабельная версия', inline=False)
    embed.add_field(name='!миники',
                    value='Узнать курс миников в жите. Версия для извращенцев', inline=False)
    await ctx.send(embed=embed)


# @bot.event
# async def on_message(message):
#     print('{0.id} {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
