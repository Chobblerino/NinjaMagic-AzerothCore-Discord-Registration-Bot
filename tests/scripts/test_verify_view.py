from ui.verify_view import VerifyView

view = VerifyView()

print("Buttons:")

for item in view.children:
    print(item.label)
    print(item.custom_id)
    print(item.style)
