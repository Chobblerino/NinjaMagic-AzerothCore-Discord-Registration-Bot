import discord
from discord import app_commands

from services.setup_service import SetupService


def register(tree, guild):
    @tree.command(
        name="setup",
        description="Post the onboarding messages.",
        guild=guild,
    )
    @app_commands.default_permissions(administrator=True)
    async def setup(
        interaction: discord.Interaction,
    ):
        await SetupService.post_onboarding(
            interaction.channel,
        )

        await interaction.response.send_message(
            "✅ Onboarding messages posted successfully.",
            ephemeral=True,
        )
