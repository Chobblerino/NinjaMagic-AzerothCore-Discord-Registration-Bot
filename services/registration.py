from constants.registration import (
    ACCOUNT_CREATED,
    PASSWORD_INVALID,
    UNKNOWN_ERROR,
    USERNAME_INVALID,
)
from database.database import Database
from services.registration_policy import check_registration_allowed
from services.soap import create_account
from utils.logger import logger
from utils.messages import get_registration_message
from utils.validation import (
    validate_password,
    validate_username,
)


def log_registration_attempt(
    discord_id,
    discord_name,
    wow_account,
    success,
    reason,
):
    logger.info(
        "Registration attempt | Discord=%s | WoW=%s | Success=%s | Reason=%s",
        discord_name,
        wow_account,
        success,
        reason,
    )

    with Database() as db:
        db.log_registration_attempt(
            discord_id,
            discord_name,
            wow_account,
            success,
            reason,
        )


def process_registration(
    interaction,
    username,
    password,
):
    #
    # Registration policy
    #
    allowed, reason = check_registration_allowed(interaction)

    if not allowed:
        log_registration_attempt(
            interaction.user.id,
            interaction.user.name,
            username,
            False,
            reason,
        )

        return False, get_registration_message(reason)

    #
    # Username validation
    #
    valid, message = validate_username(username)

    if not valid:
        log_registration_attempt(
            interaction.user.id,
            interaction.user.name,
            username,
            False,
            USERNAME_INVALID,
        )

        return False, message

    #
    # Password validation
    #
    valid, message = validate_password(password)

    if not valid:
        log_registration_attempt(
            interaction.user.id,
            interaction.user.name,
            username,
            False,
            PASSWORD_INVALID,
        )

        return False, message

    #
    # Create AzerothCore account
    #
    success, message = create_account(
        username,
        password,
    )

    if not success:
        if "already" in message.lower():
            reason = "USERNAME_ALREADY_EXISTS"
        else:
            reason = UNKNOWN_ERROR

        log_registration_attempt(
            interaction.user.id,
            interaction.user.name,
            username,
            False,
            reason,
        )

        return False, message

    #
    # Link Discord account
    #
    try:
        with Database() as db:
            db.add_account(
                interaction.user.id,
                interaction.user.name,
                username,
            )

    except Exception:
        logger.exception("Failed to link Discord account in SQLite.")
        return False, "Internal database error."

    #
    # Successful registration
    #
    log_registration_attempt(
        interaction.user.id,
        interaction.user.name,
        username,
        True,
        ACCOUNT_CREATED,
    )

    return True, message
