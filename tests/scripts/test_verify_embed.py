from ui.embeds import EmbedFactory

embed = EmbedFactory.verify()

print("Title:")
print(embed.title)

print("\nDescription:")
print(embed.description)

print("\nFields:")

for field in embed.fields:
    print(field.name)
    print(field.value)

print("\nFooter:")
print(embed.footer.text)
