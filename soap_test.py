from services.soap import create_account

success, message = create_account(
    "testaccount03",
    "Test123"
)

print(success)
print(message)
