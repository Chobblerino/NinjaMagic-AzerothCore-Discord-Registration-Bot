import discord

from ui.colours import SUCCESS
from ui.icons import PING
from version import VERSION


def build_ping_embed(latency_ms: int) -> discord.Embed:
    embed = discord.Embed(
        title=f"{PING} Pong!",
        description="The Ninja Magic Community Bot is online.",
        colour=SUCCESS,
    )

    embed.add_field(
        name="Discord Latency",
        value=f"{latency_ms} ms",
        inline=True,
    )

    embed.add_field(
        name="Version",
        value=VERSION,
        inline=True,
    )

    return embed
