# auth.py
# Handles user registration and login using a simple text file as storage.
# Each line in users.txt looks like: username,password

import os

USER_FILE = "users.txt"


def load_users():
    """Reads users.txt and returns a dictionary {username: password}.
    If the file doesn't exist yet, returns an empty dictionary."""
    users = {}
    if not os.path.exists(USER_FILE):
        return users

    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            username, password = line.split(",", 1)
            users[username] = password

    return users


def save_user(username, password):
    """Appends a new username,password line to users.txt."""
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")


def register():
    """Asks the user for a new username and password, and saves them.
    Refuses to register if the username already exists."""
    users = load_users()

    print("\n--- Register ---")
    username = input("Choose a username: ").strip()

    if username in users:
        print("That username is already taken. Please try logging in instead.")
        return False

    password = input("Choose a password: ").strip()

    if username == "" or password == "":
        print("Username and password cannot be empty.")
        return False

    save_user(username, password)
    print(f"Account created for '{username}'. You can now log in.")
    return True


def login():
    """Asks for username and password, checks them against users.txt.
    Returns True if login succeeds, False otherwise."""
    users = load_users()

    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        print(f"\nWelcome back, {username}!")
        return True
    else:
        print("Incorrect username or password.")
        return False