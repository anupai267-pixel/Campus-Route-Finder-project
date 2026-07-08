# auth.py
import os

USER_FILE = "users.txt"
MIN_PASSWORD_LENGTH = 6


def load_users():
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
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")


def register_user(username, password, confirm_password):
    """Validates and creates a new user account.
    Returns (True, success_message) or (False, error_message)."""
    users = load_users()

    if username == "":
        return False, "Username cannot be empty."
    if username in users:
        return False, "That username is already taken. Please log in instead."
    if password == "":
        return False, "Password cannot be empty."
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters long."
    if password != confirm_password:
        return False, "Passwords do not match."

    save_user(username, password)
    return True, f"Account created for '{username}'. You can now log in."


def verify_login(username, password):
    """Checks credentials against users.txt.
    Returns (username, message) on success, or (None, message) on failure."""
    users = load_users()
    if username in users and users[username] == password:
        return username, f"Welcome back, {username}!"
    return None, "Incorrect username or password."