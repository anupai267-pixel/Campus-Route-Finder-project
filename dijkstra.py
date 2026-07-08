# dijkstra.py
import heapq
from graph import get_neighbors, get_all_locations


def dijkstra_shortest_path(start, end, avoid=None):
    distances = {loc: float("inf") for loc in get_all_locations()}
    parent = {loc: None for loc in get_all_locations()}

    if start == avoid or end == avoid or start not in distances:
        return None, None

    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_location = heapq.heappop(priority_queue)

        if current_location in visited:
            continue
        visited.add(current_location)

        if current_location == end:
            break

        for neighbor, weight in get_neighbors(current_location):
            if neighbor == avoid:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current_location
                heapq.heappush(priority_queue, (new_distance, neighbor))

    if distances[end] == float("inf"):
        return None, None

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, distances[end]