import os, discord, asyncio
from clients.bot import Bot
from active import active

async def main():
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    intents = discord.Intents.all()

    bot = Bot(command_prefix='!', intents=intents)

    async with bot:
        for extension in os.listdir('./cogs'):
            if extension.endswith('.py'):
                await bot.load_extension(f'cogs.{extension[:-3]}')
        await bot.start(TOKEN)

if __name__ == '__main__':
    active()
    asyncio.run(main())