from database.database import Database
from services.auth_database import AuthDatabase
from services.soap import change_password


def get_linked_accounts(discord_id):
    with Database() as db:
        rows = db.get_accounts_by_discord_id(discord_id)

        linked_accounts = [row["wow_account"] for row in rows]

        if not linked_accounts:
            return []

        with AuthDatabase() as auth_db:
            existing_accounts = {
                account.lower()
                for account in auth_db.get_existing_accounts(linked_accounts)
            }

        valid_accounts = []

        for account in linked_accounts:
            if account.lower() in existing_accounts:
                valid_accounts.append(account)
            else:
                db.remove_account(account)

        return valid_accounts


def update_password(username, password):
    return change_password(username, password)
