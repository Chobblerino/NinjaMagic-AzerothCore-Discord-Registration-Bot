from config import (
    BOT_ADMIN_ROLE,
    CLIENT_VERSION,
    DISCORD_INVITE,
    DOWNLOAD_URL,
    EXPANSION,
    GAME_CATEGORY,
    INFORMATION_CATEGORY,
    REALM_NAME,
    REGISTRATION_CHANNEL,
    REQUIRED_DISCORD_ROLE,
    RULES_CHANNEL,
    SERVER_DESCRIPTION,
    SERVER_INFO_CHANNEL,
    SERVER_NAME,
    VERIFY_CHANNEL,
    WEBSITE_URL,
    WELCOME_CHANNEL,
)


class CommunityConfig:
    def __init__(self):
        self.server_name = SERVER_NAME
        self.server_description = SERVER_DESCRIPTION
        self.realm_name = REALM_NAME
        self.expansion = EXPANSION
        self.client_version = CLIENT_VERSION
        self.website_url = WEBSITE_URL
        self.discord_invite = DISCORD_INVITE
        self.download_url = DOWNLOAD_URL
        self.verified_role = REQUIRED_DISCORD_ROLE
        self.admin_role = BOT_ADMIN_ROLE
        self.information_category = INFORMATION_CATEGORY
        self.game_category = GAME_CATEGORY

        self.welcome_channel = WELCOME_CHANNEL
        self.rules_channel = RULES_CHANNEL
        self.verify_channel = VERIFY_CHANNEL
        self.registration_channel = REGISTRATION_CHANNEL
        self.server_info_channel = SERVER_INFO_CHANNEL


community = CommunityConfig()
