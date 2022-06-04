from discord.ext import commands
import os
import random

class Custom(commands.Cog, name='Platform Commands'):
    def __init__(self, bot):
        self.bot = bot

        # load dotenv
        from dotenv import load_dotenv
        load_dotenv()

    def check_platform(ctx):
        if ctx.guild.id == int(os.environ.get('GUILD_ID_CUSTOM_1')) or ctx.author.id == int(os.environ.get('OWNER_ID')):
            return True
        else:
            raise commands.errors.CheckFailure("This command is only available on the platform server.")

    def check_sparta(ctx):
        if ctx.guild.id == int(os.environ.get('GUILD_ID_CUSTOM_2')) or ctx.author.id == int(os.environ.get('OWNER_ID')):
            return True
        else:
            raise commands.errors.CheckFailure("This command is only available on the sparta local server.")

    @commands.command(name='f40', aliases=['friday'], brief='Description')
    @commands.check(check_platform)
    async def friday(self, ctx):
        list_of_games = ['Valorant', 'Scribble.io', 'Geoguesser', 'Poker', 'Haxball', 'Draw Battle']

        await ctx.send(random.choice(list_of_games) or 'No games found')

    @commands.command(name='sink')
    @commands.check(check_sparta)
    async def sink(self, ctx):
        await ctx.send(os.environ.get('CUSTOM_IMAGE_URL_1'))


async def setup(bot):
    await bot.add_cog(Custom(bot))
