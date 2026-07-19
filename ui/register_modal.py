import discord

from services.registration import process_registration
from ui.register_embed import (
    build_registration_error_embed,
    build_registration_success_embed,
)


class RegisterModal(discord.ui.Modal, title="Create AzerothCore Account"):
    username = discord.ui.TextInput(
        label="Username",
        placeholder="Choose a username",
        min_length=3,
        max_length=16,
        required=True,
    )

    password = discord.ui.TextInput(
        label="Password",
        placeholder="Choose a password",
        min_length=6,
        max_length=16,
        required=True,
        style=discord.TextStyle.short,
    )

    confirm_password = discord.ui.TextInput(
        label="Confirm Password",
        placeholder="Enter your password again",
        min_length=6,
        max_length=16,
        required=True,
        style=discord.TextStyle.short,
    )

    async def on_submit(self, interaction: discord.Interaction):
        if self.password.value != self.confirm_password.value:
            embed = build_registration_error_embed(
                "The passwords you entered do not match."
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True,
            )
            return

        success, message = process_registration(
            interaction,
            self.username.value.strip(),
            self.password.value,
        )

        if success:
            embed = build_registration_success_embed(message)
        else:
            embed = build_registration_error_embed(message)

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True,
        )
