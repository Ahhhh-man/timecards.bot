from discord.ext import commands
import discord, os, random

class Basic(commands.Cog, name='Basic module'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hey")
    async def adhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')
    
    @commands.command(name="ahhhh")
    async def test(self, ctx):
        await ctx.send("A" + "h"*random.randint(4, 40) + "!")
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'A wild {member.mention} has appeared!')


async def setup(bot):
    await bot.add_cog(Basic(bot))