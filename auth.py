import getpass

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "staff": {"password": "staff123", "role": "staff"},
}

def login():
    print("=== LOGIN ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    user = USERS.get(username)
    if user and user["password"] == password:
        print(f"Login success ({user['role']}).")
        return user
    print("Invalid login.")
    return None