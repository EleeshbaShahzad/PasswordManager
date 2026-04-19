import hashlib
from password_vault import VaultService

app = VaultService()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Logs")
    print("4. Exit")

    choice = input("Enter: ")

    if choice == "1":
        u = input("User: ")
        p = input("Pass: ")
        print(app.register(u, p))

    elif choice == "2":
        u = input("User: ")
        p = input("Pass: ")
        print(app.login(u, p))

    elif choice == "3":
        print(app.get_logs())

    elif choice == "4":
        break

    else:
        print("Invalid")