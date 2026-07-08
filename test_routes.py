# test_routes.py
from bfs import bfs_shortest_path
from dijkstra import dijkstra_shortest_path
from graph import get_all_locations

# Each tuple is (start, end) — feel free to add more pairs here.
test_cases = [
    ("Main Gate", "Canteen"),
    ("Main Gate", "ATL"),
    ("Hostel", "Library"),
    ("CV Raman", "Canteen"),
    ("Canteen", "Main Gate"),   # expected: no path (edges are one-way)
    ("Library", "Main Gate"),   # expected: no path (Library has no outgoing edges)
]


def path_length(path):
    return len(path) - 1 if path else None


def run_comparison():
    print(f"{'Start':<12}{'End':<12}{'BFS Path':<45}{'BFS Stops':<11}{'Dijkstra Path':<45}{'Dijkstra Dist'}")
    print("-" * 140)

    for start, end in test_cases:
        bfs_path = bfs_shortest_path(start, end)
        dijkstra_path, dijkstra_distance = dijkstra_shortest_path(start, end)

        bfs_display = " -> ".join(bfs_path) if bfs_path else "NO PATH"
        dijkstra_display = " -> ".join(dijkstra_path) if dijkstra_path else "NO PATH"
        bfs_stops = path_length(bfs_path) if bfs_path else "-"
        dijkstra_dist = f"{dijkstra_distance}m" if dijkstra_distance is not None else "-"

        print(f"{start:<12}{end:<12}{bfs_display:<45}{str(bfs_stops):<11}{dijkstra_display:<45}{dijkstra_dist}")


def run_large_map_stress_test():
    """
    A simple stress test: run Dijkstra from every location to every other
    location and confirm the program doesn't crash or hang. With a bigger
    campus map, this same test would still work unchanged.
    """
    all_locations = get_all_locations()
    total_tests = 0
    failures = 0

    for start in all_locations:
        for end in all_locations:
            if start == end:
                continue
            total_tests += 1
            try:
                dijkstra_shortest_path(start, end)
                bfs_shortest_path(start, end)
            except Exception as e:
                failures += 1
                print(f"FAILED: {start} -> {end}: {e}")

    print(f"\nStress test complete: {total_tests} routes checked, {failures} failures.")


if __name__ == "__main__":
    print("=== BFS vs Dijkstra Comparison ===\n")
    run_comparison()
    print("\n=== Stress Test (every location pair) ===")
    run_large_map_stress_test()