import os, discord
from clients.bot import Bot
from cogs.basic import Basic
from cogs.admin import Admin
from cogs.command_err_handler import CommandErrHandler


def main():
    from dotenv import load_dotenv

    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    intents = discord.Intents.all()
    intents.members = True

    bot = Bot(command_prefix='!', intents=intents)

    bot.add_cog(Basic(bot))
    bot.add_cog(Admin(bot))
    bot.add_cog(CommandErrHandler(bot))

    bot.run(TOKEN)

if __name__ == '__main__':
    main()