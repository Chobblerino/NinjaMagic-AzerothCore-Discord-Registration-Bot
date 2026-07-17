import discord
from discord import app_commands

from services.setup_service import SetupService


def register(tree, guild):
    @tree.command(
        name="setup",
        description="Configure the server onboarding channels.",
        guild=guild,
    )
    @app_commands.default_permissions(administrator=True)
    async def setup(
        interaction: discord.Interaction,
    ):
        await interaction.response.defer(
            ephemeral=True,
        )

        try:
            await SetupService.run(
                interaction.guild,
            )

            summary = discord.Embed(
                title="🥷 Setup Complete",
                description=(
                    "Ninja Magic Community Bot has successfully "
                    "configured your server."
                ),
                color=discord.Color.green(),
            )

            summary.add_field(
                name="Status",
                value=(
                    "✅ Categories verified\n"
                    "✅ Channels verified\n"
                    "✅ Onboarding messages updated"
                ),
                inline=False,
            )

            summary.set_footer(text="Your community is ready for new adventurers.")

            await interaction.followup.send(
                embed=summary,
                ephemeral=True,
            )

        except discord.Forbidden:
            await interaction.followup.send(
                (
                    "❌ **Setup failed**\n\n"
                    "The bot is missing one or more Discord permissions.\n\n"
                    "During development, giving the bot "
                    "**Administrator** is recommended."
                ),
                ephemeral=True,
            )

        except Exception:
            await interaction.followup.send(
                (
                    "❌ **Setup failed**\n\n"
                    "An unexpected error occurred.\n\n"
                    "Please check the bot logs for details."
                ),
                ephemeral=True,
            )
