import discord
from discord.ext import commands
from minerals import all_items

TOKEN = 'NzcwOTY0MjM1OTI4NzMxNjcw.X5lOZQ.HVLzOpho0waL8oU-YWqFnOU6Duw'
bot = commands.Bot(command_prefix='!')
print('Bot started')


@bot.command(pass_context=True)
async def test(ctx):
    # items = all_items()
    text = ['Tritanium   Sell {}    Buy {}\n'
            'Pyerite-----Sell {}---Buy {}\n'
            'Mexallon    Sell {}   Buy {}\n'
            'Isogen      Sell {}   Buy {}\n'
            'Nocxium     Sell {}   Buy {}\n'
            'Zydrine     Sell {}   Buy {}\n'
            'Megacyte    Sell {}   Buy {}\n'
            'Morphite    Sell {}   Buy {}\n']
    # for i in items:
    #     text.append(i)
    embed = discord.Embed(title='Твои сраные миники',
                          description=''.join(text))
    msg = await ctx.send(content='Now generating the embed...')
    await msg.edit(embed=embed, content=None)


@bot.command(pass_context=True, name='разберись')
async def info(ctx):
    msg = 'а                        ну блять под шхонки разбежалиь! тут творчесский процесс идёт! распизделись тут у меня!'
    await ctx.send(msg)


@bot.command(pass_context=True)
async def info(ctx):
    msg = 'хуиво блять! нихера ещё не сделано'
    await ctx.send(msg)

bot.run(TOKEN)
