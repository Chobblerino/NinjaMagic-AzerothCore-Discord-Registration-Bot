from database.database import Database

db = Database()
db.initialize()

accounts = db.get_accounts_by_discord_id(502419468778078230)

for account in accounts:
    print(account["wow_account"])

db.close()
