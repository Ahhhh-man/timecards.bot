from discord.ext import commands


class Bot(commands.Bot):
    async def on_ready(self):
        print("Logged in as", self.user.name, "with ID", self.user.id)
        print("Online on ", len(self.guilds), " servers:")
        for guild in self.guilds:
            print(" -", guild.name)
        print("_" * 30)
