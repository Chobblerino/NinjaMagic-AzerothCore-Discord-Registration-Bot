import discord
from discord import app_commands

from ui.help import build_home_embed
from ui.help_view import HelpView


def register(
    tree: app_commands.CommandTree,
    guild: discord.Object,
) -> None:

    @tree.command(
        name="help",
        description="Show information about the Ninja Magic Community Bot",
        guild=guild,
    )
    async def help_command(interaction: discord.Interaction):

        embed = build_home_embed()

        await interaction.response.send_message(
            embed=embed,
            view=HelpView(),
            ephemeral=True,
        )
