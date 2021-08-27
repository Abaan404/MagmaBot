import discord, os, logging
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '>', intents = intents)

logger = logging.getLogger('discord')
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, (commands.errors.MissingRequiredArgument, commands.errors.CommandNotFound, commands.errors.UserNotFound)): # Mute common errors
        pass

# Load all cogs inside ./cogs
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(os.getenv("BOT_TOKEN"))
