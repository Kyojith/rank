import config
from logging import getLogger, DEBUG, FileHandler, Formatter
from nextcord import Intents, Status, Streaming
from nextcord.ext import commands
from os import listdir
from asyncio import run

logger = getLogger("nextcord")
logger.setLevel(DEBUG)
handler = FileHandler(filename="log/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

intent = Intents.default()
intent.members = True
React = commands.Bot(
    command_prefix=config.Bot_prefix,
    case_insensitive=True,
    help_command=None,
    intents=intent,
    strip_after_prefix=True,
)

async def loadcogs():
    for file in listdir("cogs"):
        if file.endswith(".py") and not file.startswith("__COMING__SOON"):
            try:
                React.load_extension(f"cogs.{file[:-3]}")
                print(f"Successfully load {file[:-3]}")
            except Exception as e:
                print(f"Unable to load {file[:-3]} {e}")

@React.event
async def on_connect():
    print("Connected to discord API")


@React.event
async def on_ready():
    print(f"{React.user} is online")
    await React.change_presence(
        status=Status.idle,
        activity=Streaming(
            name="บอทระบบสุดเเน่นโดยSmilewinShop",
            url="https://www.twitch.tv/smilewinbot",
        ),
    )


if __name__ == "__main__":
    run(loadcogs())
    React.run(config.Token, reconnect=True)
