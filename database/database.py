import sqlite3
from pathlib import Path

from utils.logger import logger

DATABASE_FILE = Path(__file__).parent / "acore_discord.db"


class Database:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __init__(self):
        logger.info("Opening SQLite database: %s", DATABASE_FILE)

        self.connection = sqlite3.connect(DATABASE_FILE)
        self.connection.row_factory = sqlite3.Row

    def initialize(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id TEXT NOT NULL,
                discord_name TEXT NOT NULL,
                wow_account TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registration_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                discord_id TEXT NOT NULL,
                discord_name TEXT NOT NULL,
                wow_account TEXT,
                success INTEGER NOT NULL,
                reason TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    def add_account(self, discord_id, discord_name, wow_account):
        logger.info(
            "Adding SQLite link: %s -> %s",
            discord_name,
            wow_account,
        )

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO accounts (
                discord_id,
                discord_name,
                wow_account
            )
            VALUES (?, ?, ?)
            """,
            (
                str(discord_id),
                discord_name,
                wow_account,
            ),
        )

        logger.info("Rows inserted: %s", cursor.rowcount)

        self.connection.commit()

        logger.info("SQLite commit complete.")

    def remove_account(self, wow_account):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM accounts
            WHERE wow_account = ?
            """,
            (wow_account,),
        )

        self.connection.commit()

    def get_accounts_by_discord_id(self, discord_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT wow_account
            FROM accounts
            WHERE discord_id = ?
            ORDER BY wow_account
            """,
            (str(discord_id),),
        )

        return cursor.fetchall()

    def log_registration_attempt(
        self,
        discord_id,
        discord_name,
        wow_account,
        success,
        reason,
    ):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO registration_log (
                discord_id,
                discord_name,
                wow_account,
                success,
                reason
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                str(discord_id),
                discord_name,
                wow_account,
                int(success),
                reason,
            ),
        )

        self.connection.commit()

    def get_last_successful_registration(self, discord_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT created_at
            FROM registration_log
            WHERE discord_id = ?
              AND success = 1
            ORDER BY created_at DESC
            LIMIT 1
            """,
            (str(discord_id),),
        )

        return cursor.fetchone()

    def close(self):
        self.connection.close()
