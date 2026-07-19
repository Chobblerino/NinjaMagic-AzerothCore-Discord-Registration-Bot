import discord
from discord import app_commands

from ui.register_modal import RegisterModal


def register(
    tree: app_commands.CommandTree,
    guild: discord.Object,
) -> None:

    @tree.command(
        name="register",
        description="Create a new AzerothCore account",
        guild=guild,
    )
    async def register_command(interaction: discord.Interaction):
        await interaction.response.send_modal(
            RegisterModal(),
        )
