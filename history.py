# history.py
import os

HISTORY_FILE = "history.txt"


def save_history(username, start, end, method):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{username},{start},{end},{method}\n")


def get_history(username):
    if not os.path.exists(HISTORY_FILE):
        return []

    records = []
    with open(HISTORY_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 4:
                continue
            file_username, start, end, method = parts
            if file_username == username:
                records.append((start, end, method))

    return records


def clear_history(username):
    if not os.path.exists(HISTORY_FILE):
        return

    remaining_lines = []
    with open(HISTORY_FILE, "r") as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(",")
            if len(parts) != 4:
                continue
            if parts[0] != username:
                remaining_lines.append(stripped)

    with open(HISTORY_FILE, "w") as file:
        for line in remaining_lines:
            file.write(line + "\n")