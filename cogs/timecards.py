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

    async def send_timecard(self):
        for guild in self.bot.guilds:
            if guild.system_channel is not None:
                view = discord.ui.View()
                item = discord.ui.Button(
                    style=discord.ButtonStyle.gray, label="Link", url=f"https://{self.url}.com")
                view.add_item(item=item)

                await guild.system_channel.send("@everyone **Timecard Reminder!**", view=view)

    @tasks.loop(seconds=60)
    async def minute_finder(self):
        if datetime.now().minute == 0:
            self.hour_finder.start()

    @tasks.loop(hours=1)
    async def hour_finder(self):
        self.minute_finder.stop()
        self.minute_finder.cancel()
        if datetime.now().hour == 17 and datetime.now().weekday() == 4:
            await self.send_timecard()

    @commands.Cog.listener()
    async def on_ready(self):
        self.minute_finder.start()

    @commands.command(name="timecard")
    @commands.is_owner()
    async def timecard(self, ctx):
        await self.send_timecard()

async def setup(bot):
    await bot.add_cog(Timecards(bot))
