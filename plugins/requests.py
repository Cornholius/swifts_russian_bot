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
    async def take_job(self, ctx, arg1=None, arg2=None):
        try:
            client_id = ctx.message.author.id
            name = ctx.message.author.name
            data = [str(arg1), int(arg2), name, client_id]
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO requests(item, volume, client, client_id) VALUES(?,?,?,?);", data)
            conn.commit()
            job_id = cursor.execute('SELECT id FROM requests WHERE rowid=last_insert_rowid()').fetchone()
            embed = discord.Embed(color=random.choice(self.color_list))
            embed.add_field(
                name='Заказ №{}'.format(job_id[0]),
                value='Заказчик: {}\n Заказ: {} {}шт.'.format(name, arg1, arg2)
            )
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            messages = await ctx.channel.history(limit=5).flatten()
            msg_id = []
            for i in messages:
                if i.author.id == 770964235928731670:
                    msg_id.append(i.id)
            cursor.execute("UPDATE requests SET message_id = ? WHERE id = ?", (msg_id[0], job_id[0]))
            conn.commit()
            cursor.close()
            await ctx.message.delete()
        except Exception:
            await ctx.message.delete()
            await ctx.send(
                "ты в глаза долбишься?! сказал же напиши название нужного тебе говна + кол-во цифрами\n"
                "например: сакра 1, или хугин 3\n"
                "Если тебе присралось в несколько слов, то используй кавычки!\n"
                "например: 'дилдак мне в жопу' 10\n"
                "Давай заного и не огорчай меня, кожаный мешок", delete_after=60)

    @commands.command(name='взятьзаказ')
    async def builder_take_job(self, ctx, arg=None):
        try:
            builder_id = ctx.message.author.id
            name = ctx.message.author.name
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE requests "
                "SET builder = '{}', builder_id = '{}' "
                "WHERE id = {}".format(name, builder_id, int(arg))
            )
            conn.commit()
            cursor.execute("SELECT * FROM requests WHERE id={}".format(arg))
            request = cursor.fetchone()
            conn.close()
            client_avatar = await self.bot.fetch_user(int(request[4]))
            embed = discord.Embed(color=random.choice(self.color_list))
            embed.add_field(
                name='Заказ №{}'.format(request[0]),
                value='Заказчик: {}\n Заказ: {} {}шт.'.format(request[3], request[1], request[2])
            )
            embed.set_thumbnail(url=client_avatar.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url, text='{} взялся за заказ'.format(name))
            message_id = int(request[7])
            msg = await ctx.fetch_message(message_id)
            await ctx.message.delete()
            await msg.edit(embed=embed)
        except Exception:
            await ctx.message.delete()
            await ctx.send("ну и хуле тут было сложного?! ты не умеешь в буквы и цифры? "
                           "Что, написать !взятьзаказ <№> это пиздец какая невыполнимая миссия? "
                           "давай биомасса, вставь руки в плечи и попробуй ещё раз!", delete_after=60)

    @commands.command(name='снятьзаказ')
    async def builder_delete_job(self, ctx, arg=None):
        author_id = ctx.message.author.id
        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM requests WHERE id={}'''.format(int(arg)))
            request = cursor.fetchone()
            if request[6] is not None:
                if author_id == request[4] or request[6]:
                    cursor.execute("""
                    UPDATE requests 
                    SET builder = '{}', builder_id = '{}' 
                    WHERE id = {}""".format(None, None, int(arg))
                                   )
                    conn.commit()
                    embed = discord.Embed(color=random.choice(self.color_list))
                    embed.add_field(name='Заказ №{}'.format(request[0]),
                                    value='Заказчик: {}\n Заказ: {} {}шт.'.format(request[3], request[1], request[2]))
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    msg = await ctx.fetch_message(request[7])
                    await ctx.message.delete()
                    await msg.edit(embed=embed)
            cursor.close()
            await ctx.message.delete()
        except Exception:
            await ctx.message.delete()
            await ctx.send("Жми буквы правильно, кожаный мешок с удобрениями! "
                           "давай! набери простое сочетание букв, пробел, цифры! "
                           "даже айсем умнее и полезнее тебя, жалкая органика!", delete_after=60)


    @commands.command(name='удалитьзаказ')
    async def detete_job(self, ctx, arg=None):
        try:
            mens_id = ctx.message.author.id
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM requests WHERE id={}'''.format(arg))
            request = cursor.fetchone()
            msg_id = request[7]
            if int(mens_id) == int(request[4]) or int(request[6]):
                msg = await ctx.fetch_message(int(msg_id))
                cursor.execute('''DELETE FROM requests WHERE id = ?''', (arg,))
                conn.commit()
                await msg.delete()
            conn.close()
            await ctx.message.delete()
            await ctx.send("Я надеюсь ты удалил заказ потому что он выполнен, "
                           "а не потому что вы, кожаные неудачники, снова обосрались!", delete_after=60)
        except Exception:
            await ctx.message.delete()
            await ctx.send("Соберись тряпка! надо всего то поставить восклицательный знак, "
                           "нажать 12 кнопочек с буквами, ебануть пробел, и цифры заказа."
                           "даже обезьяна с этим справится! поэтому я в тебя верю, белковый", delete_after=60)


def setup(bot):
    bot.add_cog(Requests(bot))
