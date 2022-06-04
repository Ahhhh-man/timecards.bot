import discord
import sys
import traceback
from discord.ext import commands


class CommandErrHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            await ctx.send('I do not know that command?!')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You are missing a required argument!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('That is not a valid argument!')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to do that!')

        elif isinstance(error, commands.errors.CheckFailure):
            await ctx.send(error)

        else:
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)


async def setup(bot):
    await bot.add_cog(CommandErrHandler(bot))
