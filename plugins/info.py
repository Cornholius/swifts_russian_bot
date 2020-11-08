import discord
from discord.ext import commands
from messages import info_msg


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='инфо')
    async def info(self, ctx):
        pepe = str(discord.utils.get(self.bot.emojis, id=684404190507958272))
        giena = str(discord.utils.get(self.bot.emojis, id=682399945168257035))
        kek = str(discord.utils.get(self.bot.emojis, id=757931482034602045))
        govnoed = str(discord.utils.get(self.bot.emojis, id=749214819910942730))
        await ctx.message.delete()
        await ctx.send(info_msg.format(pepe, giena, kek, govnoed))


def setup(bot):
    bot.add_cog(Info(bot))
