from constants import registration as reasons

REGISTRATION_MESSAGES = {
    reasons.ACCOUNT_CREATED: "Your AzerothCore account has been created successfully.",
    reasons.USERNAME_ALREADY_EXISTS: "That username is already taken.",
    reasons.USERNAME_INVALID: "That username is not valid.",
    reasons.PASSWORD_INVALID: "That password is not valid.",
    reasons.ACCOUNT_LIMIT_REACHED: "You have reached the maximum number of linked accounts.",
    reasons.MISSING_VERIFIED_ROLE: "You must verify yourself before creating an account.",
    reasons.COOLDOWN_ACTIVE: "Please wait before creating another account.",
    reasons.DISCORD_ACCOUNT_TOO_NEW: "Your Discord account is too new to register.",
    reasons.UNKNOWN_ERROR: "An unexpected error occurred.",
}


def get_registration_message(reason):
    return REGISTRATION_MESSAGES.get(
        reason,
        REGISTRATION_MESSAGES[reasons.UNKNOWN_ERROR],
    )
