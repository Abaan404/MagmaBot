import discord, itertools
from discord.ext import commands, tasks

# Lava is not allowed to change the first text
PRESENCE_TEXT = itertools.cycle(["lava is cute", "*pushes you against wall* wanna play fortnite amongus?", "with ur mum", "owo.exe", "dangit jelly", "gewrhgkhewghkhfuckoiyo5uo", "MiEWcWAFT?? OWOWO"])

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.presence_text_loop.start()

    # A command example
    @commands.command(name = "sus", aliases = ["sussy", "amongus", "AAAA"])
    async def _sus(self, ctx, user: discord.Member):
        """
        `+sus [user]`: Sends a sus link

        ### Parameters
        ---------------
        `[user]`: discord.Member
            The member being mentioned
        """
        await ctx.send(f"Heres your link {user.mention} you sussy little baka ***pushes you against wall*** owo?\n https://youtu.be/rlkSMp7iz6c")

    # A task example
    @tasks.loop(seconds = 30)
    async def presence_text_loop(self):
        """
        Cycle through `Now playing` statuses
        """
        await self.bot.change_presence(activity = discord.Activity(type = discord.enums.ActivityType.playing, name = next(PRESENCE_TEXT)))

    @presence_text_loop.before_loop
    async def _wait(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(ExampleCog(bot))
