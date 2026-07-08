# dfs.py
from graph import get_neighbors, get_all_locations


def dfs_all_paths(start, end, path=None, all_paths=None):
    if path is None:
        path = [start]
    if all_paths is None:
        all_paths = []

    if start == end:
        all_paths.append(list(path))
        return all_paths

    for neighbor, distance in get_neighbors(start):
        if neighbor not in path:
            path.append(neighbor)
            dfs_all_paths(neighbor, end, path, all_paths)
            path.pop()

    return all_paths


def find_reachable_locations(start):
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
    all_locations = set(get_all_locations())
    report = {}

    for loc in all_locations:
        reachable = find_reachable_locations(loc)
        unreachable = all_locations - reachable - {loc}
        if unreachable:
            report[loc] = unreachable

    return report