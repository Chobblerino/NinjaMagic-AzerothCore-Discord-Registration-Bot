import discord

from services.registration import process_registration


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

    async def on_submit(self, interaction: discord.Interaction):
        success, message = process_registration(
            interaction,
            self.username.value.strip(),
            self.password.value,
        )

        if success:
            await interaction.response.send_message(
                f"✅ {message}",
                ephemeral=True,
            )
        else:
            await interaction.response.send_message(
                f"❌ {message}",
                ephemeral=True,
            )
