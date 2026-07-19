import discord

from ui.help import (
    build_account_embed,
    build_community_embed,
    build_home_embed,
    build_staff_embed,
)


class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(
        label="Account",
        emoji="⚔️",
        style=discord.ButtonStyle.primary,
    )
    async def account_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await interaction.response.edit_message(
            embed=build_account_embed(),
            view=self,
        )

    @discord.ui.button(
        label="Community",
        emoji="👥",
        style=discord.ButtonStyle.primary,
    )
    async def community_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await interaction.response.edit_message(
            embed=build_community_embed(),
            view=self,
        )

    @discord.ui.button(
        label="Staff",
        emoji="🛠",
        style=discord.ButtonStyle.secondary,
    )
    async def staff_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await interaction.response.edit_message(
            embed=build_staff_embed(),
            view=self,
        )

    @discord.ui.button(
        label="Home",
        emoji="🏠",
        style=discord.ButtonStyle.success,
    )
    async def home_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await interaction.response.edit_message(
            embed=build_home_embed(),
            view=self,
        )
