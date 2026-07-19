import discord

from services.community_config import community


class VerificationService:
    @staticmethod
    async def verify(
        interaction: discord.Interaction,
    ) -> tuple[bool, str]:
        guild = interaction.guild

        if guild is None:
            return False, "Unable to determine the Discord server."

        role = discord.utils.get(
            guild.roles,
            name=community.verified_role,
        )

        if role is None:
            return (
                False,
                f"Role '{community.verified_role}' was not found.",
            )

        member = interaction.user

        if role in member.roles:
            return (
                True,
                "✅ You are already verified.",
            )

        await member.add_roles(role)

        return (
            True,
            "✅ Verification successful! Welcome to the server.",
        )
