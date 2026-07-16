import discord

from services.community_config import community


class SetupService:
    @staticmethod
    def create_welcome_embed():
        embed = discord.Embed(
            title=f"👋 Welcome to {community.server_name}",
            description=community.server_description,
            color=discord.Color.blurple(),
        )

        embed.add_field(
            name="Getting Started",
            value=(
                "1. Read the server rules.\n"
                "2. Verify yourself.\n"
                "3. Register your AzerothCore account.\n"
                "4. Start your adventure!"
            ),
            inline=False,
        )

        embed.set_footer(
            text=f"{community.server_name} • Client {community.client_version}"
        )

        return embed
