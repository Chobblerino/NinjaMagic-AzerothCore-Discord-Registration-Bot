from services.soap import change_password

success, message = change_password(
    "testuser01",
    "NewPassword1",
)

print(success)
print(message)
