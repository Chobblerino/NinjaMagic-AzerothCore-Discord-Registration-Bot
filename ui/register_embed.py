import discord

from ui.colours import ERROR, SUCCESS
from ui.icons import ACCOUNT


def build_registration_success_embed(message: str) -> discord.Embed:
    embed = discord.Embed(
        title=f"{ACCOUNT} Registration Successful",
        description=message,
        colour=SUCCESS,
    )

    return embed


def build_registration_error_embed(message: str) -> discord.Embed:
    embed = discord.Embed(
        title=f"{ACCOUNT} Registration Failed",
        description=message,
        colour=ERROR,
    )

    return embed
