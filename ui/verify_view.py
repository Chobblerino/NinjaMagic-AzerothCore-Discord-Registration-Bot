import discord

from services.verification import VerificationService


class VerifyButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Verify",
            emoji="✔",
            style=discord.ButtonStyle.success,
            custom_id="verify_button",
        )

    async def callback(
        self,
        interaction: discord.Interaction,
    ):
        success, message = await VerificationService.verify(
            interaction,
        )

        await interaction.response.send_message(
            message,
            ephemeral=True,
        )


class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(VerifyButton())
