import mysql.connector

from config import (
    MYSQL_DATABASE,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_USER,
)


class AuthDatabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
        )

    def account_exists(self, username):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM account
            WHERE username = %s
            LIMIT 1
            """,
            (username,),
        )

        return cursor.fetchone() is not None

    def get_existing_accounts(self, usernames):
        if not usernames:
            return set()

        placeholders = ",".join(["%s"] * len(usernames))

        cursor = self.connection.cursor()

        cursor.execute(
            f"""
            SELECT username
            FROM account
            WHERE username IN ({placeholders})
            """,
            tuple(usernames),
        )

        return {row[0] for row in cursor.fetchall()}

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
