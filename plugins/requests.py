import discord
import random
from discord.ext import commands
import sqlite3


class Requests(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        self.color_list = [i[0] for i in cursor.execute("SELECT value FROM colors").fetchall()]
        cursor.close()

    @commands.command(name='заказ')
    async def take_job(self, ctx, arg1, arg2):
        try:
            client_id = ctx.message.author.id
            message_id = ctx.message.id
            name = ctx.message.author.name
            data = [str(arg1), int(arg2), name, client_id, message_id]
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("""
                    INSERT INTO requests(item, volume, client, client_id, message_id) 
                    VALUES(?,?,?,?,?);""",
                           data)
            conn.commit()
            job_id = cursor.execute('select id from requests where rowid=last_insert_rowid()').fetchone()
            cursor.close()
            embed = discord.Embed(color=random.choice(self.color_list))
            embed.add_field(name='Заказ №{}'.format(job_id[0]),
                            value='Заказчик: {}\n Заказ: {} {}шт.'.format(name, arg1, arg2))
            embed.set_thumbnail(url=ctx.author.avatar_url)
            # await ctx.message.delete()
            await ctx.send(embed=embed)
            print(discord.TextChannel.last_message_id)
            print(discord.TextChannel.last_message)

        except Exception:
            await ctx.message.delete()
            await ctx.send('''ты в глаза долбишься?! сказал же напиши название нужного тебе говна + кол-во
             цифрами (например: сакра 1, или хугин 3. Название итема без пробелов иначе на бутылку посажу).
              Давай заного и не огорчай меня, кожаный мешок''')

    @commands.command(name='взятьзаказ')
    async def builder_take_job(self, ctx, arg):
        builder_id = ctx.message.author.id
        name = ctx.message.author.name
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        # try:
        cursor.execute('''UPDATE requests SET builder = '{}', builder_id = '{}' WHERE id = {}'''
                       .format(name, builder_id, int(arg)))
        conn.commit()
        cursor.execute('''SELECT * FROM requests WHERE id={}'''.format(arg))
        request = cursor.fetchone()
        conn.close()
        embed = discord.Embed(color=random.choice(self.color_list))
        embed.add_field(name='Заказ №{}'.format(request[0]),
                        value='Заказчик: {}\n Заказ: {} {}шт.'
                        .format(request[3], request[1], request[2]))
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text='{} взялся за заказ'.format(name))
        message_id = int(request[7])
        msgid = 772505556605992981
        print(message_id, type(message_id))
        print(msgid, type(msgid))
        msg = await ctx.fetch_message(message_id)
        print('5')
        print(msg.content)
        await msg.edit(embed=embed)
        print('6')
        # await ctx.send(embed=embed)

        # except:
        #     await ctx.message.delete()
        #     await ctx.send('Ало, биомасса! глаза протри! номер заказа состоит из цифр! знаешь что такое цифры?!')

    @commands.command(name='снятьзаказ')
    async def builder_delete_job(self, ctx, arg):
        builder_id = ctx.message.author.id
        print('builder_id', type(builder_id))
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM requests WHERE id={}'''.format(arg))
        request = cursor.fetchone()
        print('request id', type(request[4]))
        print(request)
        if request[6] != None:
            if builder_id == request[4] or request[6]:
                print('sucsess')





    @commands.command(name='удалитьзаказ')
    async def detete_job(self, ctx, arg):
        mens_id = ctx.message.author.id
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM requests WHERE id={}'''.format(arg))
        request = cursor.fetchone()
        if str(mens_id) == request[4] or request[6]:
            cursor.execute('''DELETE FROM requests WHERE id = ?''', (arg,))
            conn.commit()
        conn.close()
        await ctx.message.delete()
        await ctx.send('Ну наконец то! одним бесполезным заказом от бесполезного мешка стало меньше')


def setup(bot):
    bot.add_cog(Requests(bot))
