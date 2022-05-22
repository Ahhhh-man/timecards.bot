from discord.ext import commands, tasks

import os

from datetime import datetime
import random


class Timecards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        from dotenv import load_dotenv
        load_dotenv()
        self.url = os.environ.get('TIMECARD_URL')

    @tasks.loop(seconds=5)
    async def test(self):
        pass


    @tasks.loop(seconds=60)
    async def minute_finder(self):
        if datetime.now().minute == 0:
            self.hour_finder.start()
    
    @tasks.loop(hours=1)
    async def hour_finder(self):
        self.minute_finder.stop()
        self.minute_finder.cancel()
        if datetime.now().hour == 17:
            for guild in self.bot.guilds:
                if guild.system_channel is not None:
                    await guild.system_channel.send(f"@everyone Time for timecards! {self.url}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.minute_finder.start()
        self.test.start()

