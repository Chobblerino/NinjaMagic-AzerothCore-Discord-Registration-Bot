from config import (
    BOT_ADMIN_ROLE,
    CLIENT_VERSION,
    DISCORD_INVITE,
    DOWNLOAD_URL,
    EXPANSION,
    REALM_NAME,
    REQUIRED_DISCORD_ROLE,
    SERVER_DESCRIPTION,
    SERVER_NAME,
    WEBSITE_URL,
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


community = CommunityConfig()
