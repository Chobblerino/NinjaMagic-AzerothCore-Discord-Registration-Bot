import discord
from discord import app_commands

from commands.changepassword import register as register_changepassword
from commands.myaccounts import register as register_myaccounts
from commands.register import register as register_register
from commands.setup import register as register_setup
from commands.verifytest import register as register_verifytest
from config import DISCORD_TOKEN, GUILD_ID
from database.database import Database
from utils.logger import logger
from version import VERSION


class RegistrationBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        with Database() as db:
            db.initialize()

        guild = discord.Object(id=GUILD_ID)

        register_register(
            self.tree,
            guild,
        )

        register_myaccounts(
            self.tree,
            guild,
        )

        register_changepassword(
            self.tree,
            guild,
        )

        register_verifytest(
            self.tree,
            guild,
        )

        register_setup(
            self.tree,
            guild,
        )

        synced = await self.tree.sync(guild=guild)

        logger.info("Synced %d command(s)", len(synced))

    async def on_ready(self):
        logger.info("----------------------------------------")
        logger.info("AC Registration Bot")
        logger.info("Version : %s", VERSION)
        logger.info("Logged in: %s", self.user)
        logger.info("Guild ID : %s", GUILD_ID)
        logger.info("----------------------------------------")


bot = RegistrationBot()
bot.run(DISCORD_TOKEN)
