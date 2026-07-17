import discord

from ui.embeds import EmbedFactory
from ui.verify_view import VerifyView
from utils.logger import logger


class MessageSetupService:
    @staticmethod
    async def ensure_message(
        channel: discord.TextChannel,
        embed: discord.Embed,
        view: discord.ui.View | None = None,
    ):
        footer = embed.footer.text

        async for message in channel.history(limit=25):
            if message.author != channel.guild.me:
                continue

            if not message.embeds:
                continue

            existing = message.embeds[0]

            if existing.footer and existing.footer.text == footer:
                await message.edit(
                    embed=embed,
                    view=view,
                )

                logger.info(
                    "[SETUP] Updated message: %s",
                    channel.name,
                )

                return

        await channel.send(
            embed=embed,
            view=view,
        )

        logger.info(
            "[SETUP] Created message: %s",
            channel.name,
        )

    @staticmethod
    async def populate(
        welcome: discord.TextChannel,
        rules: discord.TextChannel,
        verify: discord.TextChannel,
        registration: discord.TextChannel,
        server_info: discord.TextChannel,
    ):
        await MessageSetupService.ensure_message(
            welcome,
            EmbedFactory.welcome(),
        )

        await MessageSetupService.ensure_message(
            rules,
            EmbedFactory.rules(),
        )

        await MessageSetupService.ensure_message(
            verify,
            EmbedFactory.verify(),
            VerifyView(),
        )

        await MessageSetupService.ensure_message(
            registration,
            EmbedFactory.registration(),
        )

        await MessageSetupService.ensure_message(
            server_info,
            EmbedFactory.server_info(),
        )
