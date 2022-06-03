from discord.ext import commands
import os
import random

class Custom(commands.Cog, name='Platform Commands'):
    def __init__(self, bot):
        self.bot = bot

    def check_platform(ctx):
        # load dotenv
        from dotenv import load_dotenv
        load_dotenv()

        if ctx.guild.id == int(os.environ.get('GUILD_ID_CUSTOM_1')):
            return True
        else:
            raise commands.errors.CheckFailure("This command is only available on the platform server.")


    @commands.command(name='f40', aliases=['friday'])
    @commands.check(check_platform)
    async def friday(self, ctx):
        list_of_games = ['Valorant', 'Scribble.io', 'Geoguesser', 'Poker', 'Haxball', 'Draw Battle']

        await ctx.send(random.choice(list_of_games))


async def setup(bot):
    await bot.add_cog(Custom(bot))
