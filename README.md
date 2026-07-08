# Campus Route Finder

A command-line tool that finds the shortest route between locations on a
campus, using graph algorithms: BFS, Dijkstra's Algorithm, and DFS.

## Project Structure
- `graph.py` — stores the campus map as an adjacency list
- `bfs.py` — finds the route with the fewest stops (unweighted shortest path)
- `dijkstra.py` — finds the route with the shortest total distance (weighted shortest path)
- `dfs.py` — finds all possible routes between two points, and checks for disconnected locations
- `main.py` — the interactive menu that ties everything together
- `test_routes.py` — automated tests comparing BFS vs Dijkstra, and a stress test

## How to Run
1. Make sure Python is installed: `python --version`
2. From inside this folder, run: