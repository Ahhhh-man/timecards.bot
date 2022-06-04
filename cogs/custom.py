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

    
    @commands.command(name="clown")
    @commands.guild_only()
    async def clown(self, ctx, agent: str = None):
        CLOWN_URL = os.environ.get('CUSTOM_IMAGE_URL_2')
        clowns = {
            'breach': "/894897773575557140/breach.png",
            'cypher': "/894897784325546055/cypher.png",
            'omen': "/894897796317061170/omen.png",
            'jett': "/894897808941920306/jett.png",
            'kj': "/894897816588148736/kj.png",
            'killjoy': "/894897816588148736/kj.png",
            'phoenix': "/894897824112717834/phoenix.png",
            'raze': "/894897827354935296/raze.png",
            'sage': "/894897828911005706/sage.png",
            'viper': "/894897830093791272/viper.png",
            'reyna': "/894897830152523776/reyna.png",
            'skye': "/894897834216796190/skye.png",
            'yoru': "/894897834753675284/yoru.png"
        }

        # if the user doesnt provide an agent, then we will use a random agent
        if not agent:
            await ctx.send(CLOWN_URL + random.choice(list(clowns.values())))
        else:
        # check if the input is a valid agent
            try:
                agent_url = clowns[agent]
                await ctx.send(CLOWN_URL + agent_url)
            except KeyError:
                await ctx.send("You're the clown!")


async def setup(bot):
    await bot.add_cog(Custom(bot))
