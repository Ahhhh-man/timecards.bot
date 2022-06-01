from discord.ext import commands
import discord
import os
import random


class Basic(commands.Cog, name='Basic module'):
    def __init__(self, bot):
        self.bot = bot
        self.last_user = None

    @commands.command(name="hey")
    async def hey(self, ctx):
        if ctx.author == self.last_user:
            await ctx.send("Hey again!")
        else:
            await ctx.send(f"Hey {ctx.author.name}!")

        self.last_user = ctx.author

    @commands.command(name="ahhhh")
    async def test(self, ctx):
        await ctx.send("A" + "h"*random.randint(4, 40) + "!")

    @commands.command(name="pool")
    async def test2(self, ctx):
        # check if the users name is pool
        if ctx.author.name == "pool" and random.randint(0, 1) == 1:
            text = "Appalling"
        else:
            text = "P" + "o"*random.randint(2, 40) + "l!"

        await ctx.send(text)

async def setup(bot):
    await bot.add_cog(Basic(bot))
