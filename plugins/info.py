import random
import sqlite3

import discord
from discord.ext import commands

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
        embed = discord.Embed(title='Падаль, ты шевелишь меня ради :', color=random.choice(self.color_list))
        embed.add_field(name='!камушки',
                        value='Какие нахер камни.\n'
                              'Ты последние патчи от говножуев видел, а?', inline=False)
        embed.add_field(name='!работяги',
                        value='Инфа, по корчеванию тазов', inline=False)
        embed.add_field(name='!цена',
                        value='Шустрила чекнет цены в ЖиЖе', inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='камушки')
    async def rocks(self, ctx):
        embed = discord.Embed(title='Ты камни сосать пришел или убивать, а?\n'
                                    'Ну смотри:', color=random.choice(self.color_list))
        embed.add_field(name='!минералы',
                        value='Узнать курс миников в жите.\n'
                              'Читабельная версия', inline=False)
        embed.add_field(name='!миники',
                        value='Узнать курс миников в жите.\n'
                              'Версия для извращенцев', inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='работяги')
    async def workers(self, ctx):
        embed = discord.Embed(title='Эй, мешок волосатый, сейчас ты охуеешь от инфы:', color=random.choice(self.color_list))
        embed.add_field(name='!Заказ',
                        value='что можно, прям берешь и пишешь\n'
                              '!заказ %имя% %количество%, если в заказе 2 и более слов то "%имя%"\n'
                              'если накосячишь, гномы-работяги будут пежить тебя в очко', inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command(name='цена')
    async def prices(self, ctx):
        embed = discord.Embed(title='Сыш, ', color=random.choice(self.color_list))
        embed.add_field(name='!цена',
                        value='мешок с костями, берешь и пишешь\n'
                              '/price %name%\n'
                              'и моя шестерка тебе быстро пробьет товар в жите', inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
