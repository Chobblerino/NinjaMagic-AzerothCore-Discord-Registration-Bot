import discord

from services.community_config import community


class EmbedFactory:
    @staticmethod
    def welcome():
        embed = discord.Embed(
            title=f"⚔ Welcome to {community.server_name}",
            description=(
                f"Welcome to **{community.server_name}**!\n\n"
                "We're delighted to have you join our AzerothCore community.\n\n"
                "Whether you're returning to Northrend or beginning your first "
                "adventure, we hope you enjoy your time here."
            ),
            color=discord.Color.blurple(),
        )

        embed.add_field(
            name="📋 Getting Started",
            value=(
                "📖 **Read the Rules**\n"
                "✔ **Verify Yourself**\n"
                "📝 **Register Your Game Account**\n"
                "⚔ **Begin Your Adventure**"
            ),
            inline=False,
        )

        embed.add_field(
            name="💬 Need Help?",
            value=("If you have any questions, our community is always happy to help."),
            inline=False,
        )

        embed.set_footer(
            text=f"{community.server_name} • Client {community.client_version}"
        )

        return embed
