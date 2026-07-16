import discord
from discord import app_commands

from ui.embeds import EmbedFactory
from ui.verify_view import VerifyView


def register(tree, guild):
    @tree.command(
        name="verifytest",
        description="Post the verification message.",
        guild=guild,
    )
    @app_commands.default_permissions(administrator=True)
    async def verifytest(
        interaction: discord.Interaction,
    ):
        await interaction.channel.send(
            embed=EmbedFactory.verify(),
            view=VerifyView(),
        )

        await interaction.response.send_message(
            "✅ Verification message posted.",
            ephemeral=True,
        )
