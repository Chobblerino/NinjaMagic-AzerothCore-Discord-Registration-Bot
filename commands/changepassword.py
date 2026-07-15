import discord
from discord import app_commands

from services.accounts import get_linked_accounts
from ui.account_select import AccountSelectView
from ui.change_password_modal import ChangePasswordModal


def register(tree: app_commands.CommandTree, guild: discord.Object):

    @tree.command(
        name="changepassword",
        description="Change the password for one of your linked AzerothCore accounts",
        guild=guild,
    )
    async def changepassword(interaction: discord.Interaction):

        accounts = get_linked_accounts(interaction.user.id)

        if not accounts:
            await interaction.response.send_message(
                "❌ You don't have any linked AzerothCore accounts.",
                ephemeral=True,
            )
            return

        if len(accounts) == 1:
            await interaction.response.send_modal(
                ChangePasswordModal(accounts[0])
            )
            return

        await interaction.response.send_message(
            "Select the account you want to change the password for:",
            view=AccountSelectView(accounts),
            ephemeral=True,
        )