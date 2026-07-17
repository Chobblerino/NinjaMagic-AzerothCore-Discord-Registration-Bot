import discord

from utils.logger import logger


class GuildSetupService:
    @staticmethod
    async def get_or_create_category(
        guild: discord.Guild,
        name: str,
    ) -> discord.CategoryChannel:
        category = discord.utils.get(
            guild.categories,
            name=name,
        )

        if category is not None:
            logger.info(
                "[SETUP] Reused category: %s",
                name,
            )
            return category

        category = await guild.create_category(name)

        logger.info(
            "[SETUP] Created category: %s",
            name,
        )

        return category

    @staticmethod
    async def get_or_create_text_channel(
        category: discord.CategoryChannel,
        name: str,
    ) -> discord.TextChannel:
        channel = discord.utils.get(
            category.text_channels,
            name=name,
        )

        if channel is not None:
            logger.info(
                "[SETUP] Reused channel: %s",
                name,
            )
            return channel

        channel = await category.create_text_channel(name)

        logger.info(
            "[SETUP] Created channel: %s",
            name,
        )

        return channel
