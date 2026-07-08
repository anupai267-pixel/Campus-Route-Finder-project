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


MIN_PASSWORD_LENGTH = 6


def register():
    """Asks the user for a new username and password, with confirmation
    and basic validation. Refuses to register if the username already
    exists, the password is too short, or the two password entries don't match."""
    users = load_users()

    print("\n--- Register ---")
    username = input("Choose a username: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return False

    if username in users:
        print("That username is already taken. Please try logging in instead.")
        return False

    password = input("Choose a password: ").strip()

    if password == "":
        print("Password cannot be empty.")
        return False

    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
        return False

    confirm_password = input("Confirm your password: ").strip()

    if password != confirm_password:
        print("Passwords do not match. Please try registering again.")
        return False

    save_user(username, password)
    print(f"Account created for '{username}'. You can now log in.")
    return True


def login():
    """Asks for username and password, checks them against users.txt.
    Returns the username (string) if login succeeds, or None if it fails."""
    users = load_users()

    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        print(f"\nWelcome back, {username}!")
        return username
    else:
        print("Incorrect username or password.")
        return None