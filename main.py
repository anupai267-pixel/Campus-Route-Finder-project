# main.py
from graph import get_all_locations
from bfs import bfs_shortest_path
from dijkstra import dijkstra_shortest_path
from dfs import dfs_all_paths, check_disconnected, find_reachable_locations


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


def run_bfs():
    start, end = ask_locations()
    if start is None:
        return
    print("\n--- BFS Result (fewest stops) ---")
    print_path(bfs_shortest_path(start, end))


def run_dijkstra():
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


def show_menu():
    print("\n=== Campus Route Finder ===")
    print("1. Find shortest route by stops (BFS)")
    print("2. Find shortest route by distance (Dijkstra)")
    print("3. Show all possible routes (DFS)")
    print("4. Check for disconnected locations")
    print("5. Find route while avoiding a location")
    print("6. List all locations reachable from a point")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            run_bfs()
        elif choice == "2":
            run_dijkstra()
        elif choice == "3":
            run_dfs_all_paths()
        elif choice == "4":
            run_disconnected_check()
        elif choice == "5":
            run_avoid_route()
        elif choice == "6":
            run_reachable_from()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()