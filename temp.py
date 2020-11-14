import discord
from discord.ext import commands
from messages import info_msg


class UserAvatar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='!ава')
    async def info(self, ctx, member: discord.Member):
        print(member.display_name)


def setup(bot):
    bot.add_cog(UserAvatar(bot))
