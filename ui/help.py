import discord

from ui.colours import PRIMARY
from ui.icons import ACCOUNT, ADMIN, BOT, COMMUNITY
from version import VERSION


def build_home_embed() -> discord.Embed:
    embed = discord.Embed(
        title=f"{BOT} Ninja Magic Community Bot",
        description="Community management and AzerothCore account services.",
        colour=PRIMARY,
    )

    embed.add_field(
        name=f"{COMMUNITY} Community",
        value=("• `/help`\n• `/ping`\n• `/info`"),
        inline=False,
    )

    embed.add_field(
        name=f"{ACCOUNT} AzerothCore",
        value=("• `/register`\n• `/myaccounts`\n• `/changepassword`"),
        inline=False,
    )

    embed.add_field(
        name=f"{ADMIN} Administration",
        value=("• `/setup`\n• `/verifytest`"),
        inline=False,
    )

    embed.set_footer(text=f"Version {VERSION}")

    return embed


def build_account_embed() -> discord.Embed:
    embed = discord.Embed(
        title=f"{ACCOUNT} Account Commands",
        colour=PRIMARY,
    )

    embed.add_field(
        name="/register",
        value="Create a new AzerothCore account.",
        inline=False,
    )

    embed.add_field(
        name="/myaccounts",
        value="View your linked AzerothCore accounts.",
        inline=False,
    )

    embed.add_field(
        name="/changepassword",
        value="Change the password for one of your accounts.",
        inline=False,
    )

    return embed


def build_community_embed() -> discord.Embed:
    embed = discord.Embed(
        title=f"{COMMUNITY} Community",
        colour=PRIMARY,
    )

    embed.add_field(
        name="/help",
        value="Show this help system.",
        inline=False,
    )

    embed.add_field(
        name="/ping",
        value="Check the bot status.",
        inline=False,
    )

    return embed


def build_staff_embed() -> discord.Embed:
    embed = discord.Embed(
        title=f"{ADMIN} Staff Commands",
        colour=PRIMARY,
    )

    embed.add_field(
        name="/setup",
        value="Configure the community server.",
        inline=False,
    )

    embed.add_field(
        name="/verifytest",
        value="Test the verification workflow.",
        inline=False,
    )

    return embed
