import discord
from discord import app_commands

from ui.ping_embed import build_ping_embed


def register(
    tree: app_commands.CommandTree,
    guild: discord.Object,
) -> None:

    @tree.command(
        name="ping",
        description="Check if the bot is online",
        guild=guild,
    )
    async def ping_command(interaction: discord.Interaction):

        latency_ms = round(interaction.client.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            description="The Ninja Magic Community Bot is online.",
            colour=discord.Colour.green(),
        )

        embed.add_field(
            name="Discord Latency",
            value=f"{latency_ms} ms",
            inline=True,
        )

        embed = build_ping_embed(latency_ms)

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True,
        )
