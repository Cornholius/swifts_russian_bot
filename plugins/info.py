import discord
import random
from discord.ext import commands
import sqlite3
from discord import TextChannel

client = discord.Client()



class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        self.color_list = [i[0] for i in cursor.execute("SELECT value FROM colors").fetchall()]
        cursor.close()

    @commands.command(name='инфо')
    async def info(self, ctx):
        qwe = ctx.message.id
        embed = discord.Embed(title='Тебе, кожаный мешок, разрешается узнать:', color=random.choice(self.color_list))
        embed.add_field(name='!минералы',
                        value='Узнать курс миников в жите. Читабельная версия', inline=False)
        embed.add_field(name='!миники',
                        value='Узнать курс миников в жите. Версия для извращенцев', inline=False)
        await ctx.message.delete()
        await ctx.send(qwe, embed=embed)

    @commands.command(pass_context=True, name='qwe')
    async def qwe(self, ctx):
        messages = await ctx.channel.history
        print(messages)

def setup(bot):
    bot.add_cog(Info(bot))
