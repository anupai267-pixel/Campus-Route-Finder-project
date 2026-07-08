# bfs.py
from collections import deque
from graph import get_neighbors


def bfs_shortest_path(start, end, avoid=None):
    if start == avoid or end == avoid:
        return None

    visited = {start}
    queue = deque()
    queue.append([start])

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            return path

        for neighbor, distance in get_neighbors(current):
            if neighbor == avoid:
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)

    return None