import discord

from ui.embeds import EmbedFactory
from ui.verify_view import VerifyView


class SetupService:
    @staticmethod
    async def post_onboarding(
        channel: discord.TextChannel,
    ):
        await channel.send(
            embed=EmbedFactory.welcome(),
        )

        await channel.send(
            embed=EmbedFactory.rules(),
        )

        await channel.send(
            embed=EmbedFactory.verify(),
            view=VerifyView(),
        )

        await channel.send(
            embed=EmbedFactory.registration(),
        )

        await channel.send(
            embed=EmbedFactory.server_info(),
        )
