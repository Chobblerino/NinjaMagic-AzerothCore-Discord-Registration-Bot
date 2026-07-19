import discord

from services.accounts import update_password
from utils.validation import validate_password


class ChangePasswordModal(
    discord.ui.Modal,
    title="Change Password",
):
    password = discord.ui.TextInput(
        label="New Password",
        placeholder="Enter a new password",
        min_length=6,
        max_length=16,
        required=True,
        style=discord.TextStyle.short,
    )

    confirm_password = discord.ui.TextInput(
        label="Confirm Password",
        placeholder="Re-enter your new password",
        min_length=6,
        max_length=16,
        required=True,
        style=discord.TextStyle.short,
    )

    def __init__(self, username):
        super().__init__()
        self.username = username

    async def on_submit(self, interaction: discord.Interaction):
        password = self.password.value
        confirm_password = self.confirm_password.value

        if password != confirm_password:
            await interaction.response.send_message(
                "❌ Passwords do not match.",
                ephemeral=True,
            )
            return

        valid, message = validate_password(password)

        if not valid:
            await interaction.response.send_message(
                f"❌ {message}",
                ephemeral=True,
            )
            return

        success, message = update_password(
            self.username,
            password,
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
