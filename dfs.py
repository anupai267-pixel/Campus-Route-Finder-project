# dfs.py
from graph import get_neighbors, get_all_locations


def dfs_all_paths(start, end, path=None, all_paths=None):
    """
    Recursively explores every possible route from start to end.
    Returns a list of paths (each path is a list of location names).
    """
    if path is None:
        path = [start]
    if all_paths is None:
        all_paths = []

    if start == end:
        all_paths.append(list(path))
        return all_paths

    for neighbor, distance in get_neighbors(start):
        if neighbor not in path:  # avoid going in circles
            path.append(neighbor)
            dfs_all_paths(neighbor, end, path, all_paths)
            path.pop()  # backtrack: remove neighbor before trying the next option

    return all_paths


def find_reachable_locations(start):
    """Returns the set of every location you can reach from 'start'."""
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for neighbor, distance in get_neighbors(current):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


def check_disconnected():
    """
    Checks every location in the graph and reports which other locations
    it CANNOT reach. Returns a dictionary: {location: set_of_unreachable_locations}.
    Only locations with at least one unreachable target are included.
    """
    all_locations = set(get_all_locations())
    report = {}

    for loc in all_locations:
        reachable = find_reachable_locations(loc)
        unreachable = all_locations - reachable - {loc}
        if unreachable:
            report[loc] = unreachable

    return report