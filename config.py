import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

SOAP_HOST = os.getenv("SOAP_HOST")
SOAP_PORT = int(os.getenv("SOAP_PORT", "7878"))
SOAP_USERNAME = os.getenv("SOAP_USERNAME")
SOAP_PASSWORD = os.getenv("SOAP_PASSWORD")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

MAX_ACCOUNTS_PER_DISCORD = int(os.getenv("MAX_ACCOUNTS_PER_DISCORD", "5"))

REGISTRATION_COOLDOWN_MINUTES = int(os.getenv("REGISTRATION_COOLDOWN_MINUTES", "15"))

REQUIRED_DISCORD_ROLE = os.getenv(
    "REQUIRED_DISCORD_ROLE",
    "Verified",
)

BOT_ADMIN_ROLE = os.getenv(
    "BOT_ADMIN_ROLE",
    "Bot Admin",
)

MINIMUM_DISCORD_ACCOUNT_AGE_DAYS = int(
    os.getenv("MINIMUM_DISCORD_ACCOUNT_AGE_DAYS", "7")
)
