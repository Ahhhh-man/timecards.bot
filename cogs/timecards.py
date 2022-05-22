from discord.ext import commands, tasks
import os
import discord
from datetime import datetime


class Timecards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        from dotenv import load_dotenv
        load_dotenv()
        self.url = os.environ.get('TIMECARD_URL')

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
                    view = discord.ui.View()
                    item = discord.ui.Button(
                        style=discord.ButtonStyle.gray, label="Link", url=self.url)
                    view.add_item(item=item)

                    await guild.system_channel.send("@everyone **Timecard Reminder!**", view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        self.minute_finder.start()


async def setup(bot):
    await bot.add_cog(Timecards(bot))
