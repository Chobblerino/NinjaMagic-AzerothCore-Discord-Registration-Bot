import discord


class VerifyButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Verify",
            emoji="✔",
            style=discord.ButtonStyle.success,
            custom_id="verify_button",
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            (
                "✅ Verification is not connected yet.\n\n"
                "This will be implemented in a later RC1 step."
            ),
            ephemeral=True,
        )


class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(VerifyButton())
