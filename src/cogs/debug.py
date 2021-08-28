from discord.ext import commands

class Debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "ping")
    async def _ping(self, ctx):
        """
        `+ping`: Ping the bot
        """
        await ctx.send(f'**Pong!** *{round(self.bot.latency*1000, 4)} ms*')

def setup(bot):
    bot.add_cog(Debug(bot))