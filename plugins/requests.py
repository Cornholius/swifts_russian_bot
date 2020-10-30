import discord
import random
from discord.ext import commands
from main import color_list
import sqlite3

class Requests(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='заказ')
    async def takejob(self, ctx, arg1, arg2):
        try:
            embed = discord.Embed(title='Заказ №{}', color=random.choice(color_list))
            embed.add_field(name='Заказчик: {}'.format(ctx.message.author.name),
                            value='Заказ: {} {}шт.'.format(str(arg1), int(arg2)))
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text='{} взялся за заказ'.format(ctx.message.author.name),
                             icon_url=ctx.author.avatar_url)
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO requests(userid, fname, lname, gender) 
                                VALUES('00001', 'Alex', 'Smith', 'male');""")
            conn.commit()
            await ctx.send(embed=embed)
        except:
            await ctx.send('''ты в глаза долбишься?! сказал же напиши название нужного тебе говна + кол-во
             цифрами (например: сакра 1, или хугин 3. Название итема без пробелов иначе на бутылку посажу).
              Давай заного и не огорчай меня, кожаный мешок''')

def setup(bot):
    bot.add_cog(Requests(bot))
