import re

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 16

MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 16

RESERVED_USERNAMES = {
    "admin",
    "administrator",
    "gm",
    "console",
    "root",
    "system",
}


def validate_username(username):
    username = username.strip()

    if not re.fullmatch(
        rf"[A-Za-z0-9]{{{MIN_USERNAME_LENGTH},{MAX_USERNAME_LENGTH}}}",
        username,
    ):
        return (
            False,
            f"Username must be {MIN_USERNAME_LENGTH}-{MAX_USERNAME_LENGTH} "
            "characters and contain only letters and numbers.",
        )

    if username.lower() in RESERVED_USERNAMES:
        return (
            False,
            "That username is reserved. Please choose another.",
        )

    return True, ""


def validate_password(password):
    if not (
        MIN_PASSWORD_LENGTH
        <= len(password)
        <= MAX_PASSWORD_LENGTH
    ):
        return (
            False,
            f"Password must be between "
            f"{MIN_PASSWORD_LENGTH} and "
            f"{MAX_PASSWORD_LENGTH} characters.",
        )

    return True, ""