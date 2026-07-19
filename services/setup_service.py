import discord

from services.community_config import community
from services.guild_setup import GuildSetupService
from services.message_setup import MessageSetupService


class SetupService:
    @staticmethod
    async def run(
        guild: discord.Guild,
    ):
        #
        # Categories
        #

        information = await GuildSetupService.get_or_create_category(
            guild,
            community.information_category,
        )

        game = await GuildSetupService.get_or_create_category(
            guild,
            community.game_category,
        )

        #
        # Channels
        #

        welcome = await GuildSetupService.get_or_create_text_channel(
            information,
            community.welcome_channel,
        )

        rules = await GuildSetupService.get_or_create_text_channel(
            information,
            community.rules_channel,
        )

        verify = await GuildSetupService.get_or_create_text_channel(
            information,
            community.verify_channel,
        )

        registration = await GuildSetupService.get_or_create_text_channel(
            game,
            community.registration_channel,
        )

        server_info = await GuildSetupService.get_or_create_text_channel(
            game,
            community.server_info_channel,
        )

        #
        # Post onboarding
        #

        await MessageSetupService.populate(
            welcome,
            rules,
            verify,
            registration,
            server_info,
        )
