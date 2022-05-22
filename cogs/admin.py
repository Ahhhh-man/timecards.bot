from discord.ext import commands

class Admin(commands.Cog):

    # delete all messages in a channel
    @commands.command(name='purge', aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        