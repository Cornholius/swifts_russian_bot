import discord
import random
from discord.ext import commands
from minerals import all_items, all_id
import sqlite3


class Minerals(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        self.color_list = [i[0] for i in cursor.execute("SELECT value FROM colors").fetchall()]
        cursor.close()

    @commands.command(pass_context=True, name='миники')
    async def minerals(self, ctx):
        msg = await ctx.send(content='Щас чекнем твоё говно...')
        buy = all_items()[0]
        sell = all_items()[1]
        embed = discord.Embed(title='Твои сраные миники', color=random.choice(self.color_list))
        for key in all_id:
            embed.add_field(name=key, value='Sell: {} // Buy: {}'.format(sell[key], buy[key]), inline=False)
        await ctx.message.delete()
        await msg.edit(embed=embed, content=None)


def setup(bot):
    bot.add_cog(Minerals(bot))


if __name__ == "__main__":
    all_items()
