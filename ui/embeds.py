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

    @staticmethod
    def rules():
        embed = discord.Embed(
            title="📜 Rules of the Realm",
            description=(
                "Welcome, adventurer!\n\n"
                "Our goal is to create a friendly, respectful and enjoyable "
                "community for everyone."
            ),
            color=discord.Color.gold(),
        )

        embed.add_field(
            name="⚔ Community Rules",
            value=(
                "**1.** Respect other players.\n"
                "**2.** No cheating, exploiting or botting.\n"
                "**3.** Keep chat friendly and welcoming.\n"
                "**4.** Use the correct Discord channels.\n"
                "**5.** Respect staff decisions.\n"
                "**6.** No harassment or hate speech.\n"
                "**7.** No advertising without permission.\n"
                "**8.** Keep character names appropriate.\n"
                "**9.** Help new players whenever you can.\n"
                "**10.** Above all... **Don't be a dick.** 😄"
            ),
            inline=False,
        )

        embed.add_field(
            name="❤️ Thank You",
            value=(
                "We're excited to have you here. "
                "Let's build an amazing community together!"
            ),
            inline=False,
        )

        embed.set_footer(text=f"{community.server_name} • Community Rules")

        return embed

    @staticmethod
    def registration():
        embed = discord.Embed(
            title="📝 Register Your Game Account",
            description=(
                "You're only a few moments away from beginning your adventure.\n\n"
                "Use the commands below to manage your AzerothCore accounts."
            ),
            color=discord.Color.blue(),
        )

        embed.add_field(
            name="🆕 Create an Account",
            value="`/register`",
            inline=False,
        )

        embed.add_field(
            name="👤 My Accounts",
            value="`/myaccounts`",
            inline=False,
        )

        embed.add_field(
            name="🔑 Change Password",
            value="`/changepassword`",
            inline=False,
        )

        embed.add_field(
            name="⚔ Ready to Play?",
            value=(
                f"Launch your **{community.client_version}** client "
                "and begin your adventure!"
            ),
            inline=False,
        )

        embed.set_footer(text=f"{community.server_name} • Registration")

        return embed

    @staticmethod
    def server_info():
        embed = discord.Embed(
            title="🌍 Server Information",
            description=("Everything you need to start your adventure."),
            color=discord.Color.teal(),
        )

        embed.add_field(
            name="🏰 Realm",
            value=community.realm_name,
            inline=True,
        )

        embed.add_field(
            name="📦 Expansion",
            value=community.expansion,
            inline=True,
        )

        embed.add_field(
            name="💿 Client",
            value=community.client_version,
            inline=True,
        )

        embed.add_field(
            name="🌐 Website",
            value=community.website_url or "*Not configured*",
            inline=False,
        )

        embed.add_field(
            name="⬇ Download",
            value=community.download_url or "*Not configured*",
            inline=False,
        )

        embed.add_field(
            name="💬 Discord",
            value=community.discord_invite or "*Not configured*",
            inline=False,
        )

        embed.set_footer(text=f"{community.server_name} • Server Information")

        return embed

    @staticmethod
    def verify():
        embed = discord.Embed(
            title="✔ Verify Your Account",
            description=(
                "Before you can access the full Discord server, "
                "please verify yourself.\n\n"
                "Verification helps us keep the community welcoming "
                "and free from spam."
            ),
            color=discord.Color.green(),
        )

        embed.add_field(
            name="After Verification",
            value=(
                "✅ Access all community channels\n"
                "✅ Register your AzerothCore account\n"
                "✅ View server information\n"
                "✅ Join the adventure!"
            ),
            inline=False,
        )

        embed.add_field(
            name="Ready?",
            value=("Click the **Verify** button below to continue."),
            inline=False,
        )

        embed.set_footer(text=f"{community.server_name} • Verification")

        return embed
