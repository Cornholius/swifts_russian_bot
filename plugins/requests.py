import discord
import random
from discord.ext import commands
import sqlite3
from messages import create_job_error


class Requests(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        self.color_list = [i[0] for i in cursor.execute("SELECT value FROM colors").fetchall()]
        cursor.close()

    @commands.command(name='заказ')
    async def create_job(self, ctx, arg1=None, arg2=None):
        try:
            client_id = ctx.message.author.id
            client_name = ctx.message.author.name
            data = [str(arg1), int(arg2), client_name, client_id]
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO requests(item, volume, client, client_id) VALUES(?,?,?,?);", data)
            conn.commit()
            job_id = cursor.execute('SELECT id FROM requests WHERE rowid=last_insert_rowid()').fetchone()
            embed = discord.Embed(color=random.choice(self.color_list))
            embed.add_field(
                name='Заказ №{}'.format(job_id[0]),
                value='Заказчик: {}\n Заказ: {} {}шт.'.format(client_name, arg1, arg2)
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
            await ctx.send(create_job_error, delete_after=60)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        add_and_dell_builder = [684404190507958272, 682399945168257035]
        cancel_and_delete_job = [749214819910942730, 757931482034602045]
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        if payload.emoji.id in add_and_dell_builder:
            await self.add_or_dell_builder(conn, cursor, payload)
        if payload.emoji.id in cancel_and_delete_job:
            await self.cancel_or_delete_job(conn, cursor, payload)
        conn.close()

    async def cancel_or_delete_job(self, conn, cursor, payload):
        if payload.emoji.id == 757931482034602045:  # finish job emoji
            cursor.execute("SELECT * FROM requests WHERE message_id = {}".format(payload.message_id))
            request = cursor.fetchone()
            client = await self.bot.fetch_user(payload.member.id)
            await client.send('Заказ №{} ({} {}шт.) готов.'.format(request[0], request[1], request[2]))
        cursor.execute('''DELETE FROM requests WHERE message_id={}'''.format(payload.message_id))
        conn.commit()
        channel = self.bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        await msg.delete()

    async def add_or_dell_builder(self, conn, cursor, payload):
        if payload.emoji.id == 684404190507958272:  # add_builder rmoji
            format_data = [payload.member.name, payload.member.id, payload.message_id]
        else:  # delete_builder rmoji
            format_data = [None, None, payload.message_id]
        cursor.execute(
            "UPDATE requests "
            "SET builder = '{}', builder_id = '{}' "
            "WHERE message_id = {}".format(format_data[0], format_data[1], format_data[2])
        )
        conn.commit()
        cursor.execute("SELECT * FROM requests WHERE message_id={}".format(payload.message_id))
        request = cursor.fetchone()
        client_avatar = await self.bot.fetch_user(int(request[4]))
        builder_avatar = ''
        if payload.emoji.id == 684404190507958272:  # add_builder rmoji
            builder_avatar = await self.bot.fetch_user(int(request[6]))
        embed = discord.Embed(color=random.choice(self.color_list))
        embed.add_field(
            name='Заказ №{}'.format(request[0]),
            value='Заказчик: {}\n Заказ: {} {}шт.'.format(request[3], request[1], request[2])
        )
        embed.set_thumbnail(url=client_avatar.avatar_url)
        if payload.emoji.id == 684404190507958272:  # add_builder rmoji
            embed.set_footer(icon_url=builder_avatar.avatar_url, text='{} взялся за заказ'.format(payload.member.name))
        channel = self.bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        await msg.remove_reaction(payload.emoji, payload.member)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Requests(bot))
