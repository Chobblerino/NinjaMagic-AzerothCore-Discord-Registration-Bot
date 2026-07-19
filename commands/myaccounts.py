import discord
from discord import app_commands

from services.accounts import get_linked_accounts


def register(
    tree: app_commands.CommandTree,
    guild: discord.Object,
) -> None:

    @tree.command(
        name="myaccounts",
        description="Show your linked AzerothCore accounts",
        guild=guild,
    )
    async def myaccounts(interaction: discord.Interaction):

        accounts = get_linked_accounts(interaction.user.id)

        if not accounts:
            await interaction.response.send_message(
                "You don't have any linked AzerothCore accounts.",
                ephemeral=True,
            )
            return

        message = "🎮 **Your linked AzerothCore accounts**\n\n"

        for account in accounts:
            message += f"• {account}\n"

        await interaction.response.send_message(
            message,
            ephemeral=True,
        )
