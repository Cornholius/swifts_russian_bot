import discord
import random
from discord.ext import commands
from main import color_list


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='инфо')
    async def info(self, ctx):
        embed = discord.Embed(title='Тебе, кожаный мешок, разрешается узнать:', color=random.choice(color_list))
        embed.add_field(name='!минералы',
                        value='Узнать курс миников в жите. Читабельная версия', inline=False)
        embed.add_field(name='!миники',
                        value='Узнать курс миников в жите. Версия для извращенцев', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
