from datetime import datetime, timedelta, timezone

from config import (
    BOT_ADMIN_ROLE,
    MAX_ACCOUNTS_PER_DISCORD,
    MINIMUM_DISCORD_ACCOUNT_AGE_DAYS,
    REGISTRATION_COOLDOWN_MINUTES,
    REQUIRED_DISCORD_ROLE,
)
from constants.registration import (
    ACCOUNT_LIMIT_REACHED,
    COOLDOWN_ACTIVE,
    DISCORD_ACCOUNT_TOO_NEW,
    MISSING_VERIFIED_ROLE,
)
from database.database import Database
from services.accounts import get_linked_accounts


def is_registration_admin(member):
    if member.guild_permissions.administrator:
        return True

    return any(role.name == BOT_ADMIN_ROLE for role in member.roles)


def check_required_role(member):
    if any(role.name == REQUIRED_DISCORD_ROLE for role in member.roles):
        return True, None

    return False, MISSING_VERIFIED_ROLE


def check_account_limit(discord_id):
    accounts = get_linked_accounts(discord_id)

    if len(accounts) >= MAX_ACCOUNTS_PER_DISCORD:
        return False, ACCOUNT_LIMIT_REACHED

    return True, None


def check_registration_cooldown(discord_id):
    with Database() as db:
        row = db.get_last_successful_registration(discord_id)

    if row is None:
        return True, None

    last_registration = datetime.fromisoformat(row["created_at"])
    expires = last_registration + timedelta(minutes=REGISTRATION_COOLDOWN_MINUTES)

    if datetime.now() >= expires:
        return True, None

    return False, COOLDOWN_ACTIVE


def check_discord_account_age(user):
    minimum_date = datetime.now(timezone.utc) - timedelta(
        days=MINIMUM_DISCORD_ACCOUNT_AGE_DAYS
    )

    if user.created_at >= minimum_date:
        return False, DISCORD_ACCOUNT_TOO_NEW

    return True, None


def check_registration_allowed(interaction):
    if is_registration_admin(interaction.user):
        return True, None

    checks = (
        lambda: check_required_role(interaction.user),
        lambda: check_discord_account_age(interaction.user),
        lambda: check_account_limit(interaction.user.id),
        lambda: check_registration_cooldown(interaction.user.id),
    )

    for check in checks:
        allowed, reason = check()

        if not allowed:
            return False, reason

    return True, None
