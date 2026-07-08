# main.py
from history import save_history, get_history, clear_history
from graph import get_all_locations
from bfs import bfs_shortest_path
from dijkstra import dijkstra_shortest_path
from dfs import dfs_all_paths, check_disconnected, find_reachable_locations
from auth import login, register
from history import save_history, get_history


def print_path(path):
    if path is None:
        print("No path found between these two locations.")
    else:
        print(" -> ".join(path))
        print(f"Number of stops (hops): {len(path) - 1}")


def ask_locations():
    print("Available locations:")
    for loc in get_all_locations():
        print(" -", loc)
    start = input("\nEnter start location: ").strip()
    end = input("Enter destination: ").strip()

    all_locations = get_all_locations()
    if start not in all_locations or end not in all_locations:
        print("\nOne of those location names doesn't match exactly. "
              "Please copy a name from the list above.")
        return None, None
    return start, end


def run_bfs(username):
    start, end = ask_locations()
    if start is None:
        return
    print("\n--- BFS Result (fewest stops) ---")
    path = bfs_shortest_path(start, end)
    print_path(path)
    if path is not None:
        save_history(username, start, end, "BFS")


def run_dijkstra(username):
    start, end = ask_locations()
    if start is None:
        return
    print("\n--- Dijkstra Result (shortest distance) ---")
    path, total_distance = dijkstra_shortest_path(start, end)
    if path is None:
        print("No path found between these two locations.")
    else:
        print(" -> ".join(path))
        print(f"Total distance: {total_distance} meters")
        save_history(username, start, end, "Dijkstra")


def run_dfs_all_paths():
    start, end = ask_locations()
    if start is None:
        return
    paths = dfs_all_paths(start, end)
    print(f"\n--- DFS: All Possible Paths ({len(paths)} found) ---")
    if not paths:
        print("No path found between these two locations.")
    for i, path in enumerate(paths, start=1):
        print(f"{i}. {' -> '.join(path)}")


def run_disconnected_check():
    print("\n--- Disconnected Graph Check ---")
    report = check_disconnected()
    if not report:
        print("Every location can reach every other location.")
    else:
        for loc, unreachable in report.items():
            print(f"{loc} CANNOT reach: {', '.join(sorted(unreachable))}")


def run_avoid_route():
    start, end = ask_locations()
    if start is None:
        return
    print("Available locations:")
    for loc in get_all_locations():
        print(" -", loc)
    avoid = input("Enter a location to AVOID: ").strip()

    print(f"\n--- Route avoiding '{avoid}' ---")
    print("BFS (fewest stops):")
    print_path(bfs_shortest_path(start, end, avoid=avoid))

    print("\nDijkstra (shortest distance):")
    path, total_distance = dijkstra_shortest_path(start, end, avoid=avoid)
    if path is None:
        print("No path found between these two locations (with the avoided location removed).")
    else:
        print(" -> ".join(path))
        print(f"Total distance: {total_distance} meters")


def run_reachable_from():
    print("Available locations:")
    for loc in get_all_locations():
        print(" -", loc)
    start = input("Enter a location: ").strip()
    if start not in get_all_locations():
        print("That location name doesn't match exactly.")
        return

    reachable = find_reachable_locations(start)
    reachable.discard(start)
    print(f"\n--- Locations reachable from {start} ---")
    if not reachable:
        print("No other locations are reachable from here.")
    else:
        for loc in sorted(reachable):
            print(" -", loc)


def run_view_history(username):
    records = get_history(username)
    print(f"\n--- Route History for {username} ---")
    if not records:
        print("You haven't searched any routes yet.")
    else:
        for i, (start, end, method) in enumerate(records, start=1):
            print(f"{i}. [{method}] {start} -> {end}")


def run_clear_history(username):
    confirm = input(f"Are you sure you want to delete ALL of your route history, {username}? (yes/no): ").strip().lower()
    if confirm == "yes":
        clear_history(username)
        print("Your route history has been cleared.")
    else:
        print("Cancelled. Your history was not changed.")


def show_menu():
    print("\n=== Campus Route Finder ===")
    print("1. Find shortest route by stops (BFS)")
    print("2. Find shortest route by distance (Dijkstra)")
    print("3. Show all possible routes (DFS)")
    print("4. Check for disconnected locations")
    print("5. Find route while avoiding a location")
    print("6. List all locations reachable from a point")
    print("7. View my route history")
    print("8. Clear my route history")
    print("9. Logout")
    print("10. Exit program")


def main(username):
    """Runs the route finder menu for the given logged-in username.
    Returns 'logout' or 'exit' depending on what the user chose."""
    while True:
        show_menu()
        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            run_bfs(username)
        elif choice == "2":
            run_dijkstra(username)
        elif choice == "3":
            run_dfs_all_paths()
        elif choice == "4":
            run_disconnected_check()
        elif choice == "5":
            run_avoid_route()
        elif choice == "6":
            run_reachable_from()
        elif choice == "7":
            run_view_history(username)
        elif choice == "8":
            run_clear_history(username)
        elif choice == "9":
            print("Logging out...")
            return "logout"
        elif choice == "10":
            return "exit"
        else:
            print("Invalid choice, please enter a number from 1 to 10.")


def show_auth_menu():
    print("\n=== Welcome to Campus Route Finder ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")


def authenticate():
    """Loops until the user successfully logs in, registers, or exits.
    Returns the logged-in username (string) on success, or None if they chose to exit."""
    while True:
        show_auth_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            username = login()
            if username is not None:
                return username
        elif choice == "2":
            register()
        elif choice == "3":
            return None
        else:
            print("Invalid choice, please enter 1, 2, or 3.")


if __name__ == "__main__":
    while True:
        current_user = authenticate()
        if current_user is None:
            print("Goodbye!")
            break

        result = main(current_user)

        if result == "exit":
            print("Goodbye!")
            break
        # if result == "logout", the outer while loop goes back to
        # authenticate() automatically, showing the login screen again