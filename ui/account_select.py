import discord

from ui.change_password_modal import ChangePasswordModal


class AccountSelect(discord.ui.Select):
    def __init__(self, accounts):
        options = [
            discord.SelectOption(
                label=account,
                value=account,
            )
            for account in accounts
        ]

        super().__init__(
            placeholder="Select an account...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(
            ChangePasswordModal(
                self.values[0],
            )
        )


class AccountSelectView(discord.ui.View):
    def __init__(self, accounts):
        super().__init__()

        self.add_item(
            AccountSelect(accounts)
        )