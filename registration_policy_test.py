from services.registration_policy import check_account_limit

allowed, message = check_account_limit(
    502419468778078230
)

print(allowed)
print(message)