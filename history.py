# history.py
# Stores and retrieves each user's past searched routes.
# Each line in history.txt looks like: username,start,end,method

HISTORY_FILE = "history.txt"


def save_history(username, start, end, method):
    """Appends one route search record to history.txt."""
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{username},{start},{end},{method}\n")


def get_history(username):
    """Returns a list of (start, end, method) tuples for this username only.
    Returns an empty list if the file doesn't exist or the user has no history."""
    import os
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
                continue  # skip malformed lines instead of crashing
            file_username, start, end, method = parts
            if file_username == username:
                records.append((start, end, method))

    return records

def clear_history(username):
    """Removes all history entries for this username, keeping everyone
    else's entries intact. Rewrites history.txt without this user's lines."""
    import os
    if not os.path.exists(HISTORY_FILE):
        return  # nothing to clear

    remaining_lines = []
    with open(HISTORY_FILE, "r") as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(",")
            if len(parts) != 4:
                continue
            file_username = parts[0]
            if file_username != username:
                remaining_lines.append(stripped)

    # Rewrite the whole file with only the lines that DON'T belong to this user
    with open(HISTORY_FILE, "w") as file:
        for line in remaining_lines:
            file.write(line + "\n")