# bfs.py
from collections import deque
from graph import get_neighbors

def bfs_shortest_path(start, end, avoid=None):
    """
    Finds the path with the fewest stops between start and end.
    'avoid' is an optional location name to skip completely (used later, Day 28).
    Returns a list of location names representing the path, or None if no path exists.
    """
    if start == avoid or end == avoid:
        return None

    visited = {start}
    queue = deque()
    queue.append([start])  # we store the whole path so far in the queue

    while queue:
        path = queue.popleft()
        current = path[-1]  # last location in this path

        if current == end:
            return path

        for neighbor, distance in get_neighbors(current):
            if neighbor == avoid:
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)

    return None  # queue emptied out, destination never reached