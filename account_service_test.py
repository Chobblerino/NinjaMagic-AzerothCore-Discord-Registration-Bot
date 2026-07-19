from services.accounts import get_linked_accounts

accounts = get_linked_accounts(502419468778078230)

for account in accounts:
    print(account)
