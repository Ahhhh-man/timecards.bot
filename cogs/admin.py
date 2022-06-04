from discord.ext import commands


class Admin(commands.Cog, name='Admin Commands'):

    # delete all messages in a channel
    @commands.command(name='purge', aliases=['clear'])
    @commands.is_owner()
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @commands.command(name='say')
    @commands.is_owner()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)
    

async def setup(bot):
    await bot.add_cog(Admin(bot))
