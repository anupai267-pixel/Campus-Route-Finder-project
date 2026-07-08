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

## Login / Registration (Extra Addition)
As a separate addition on top of the core roadmap project, a simple
username/password login system was added using `auth.py`. This is a
beginner-level, file-based system — not intended for real security use.

- `auth.py` — handles registering new users and logging in
- `users.txt` — stores registered usernames and passwords as plain text
  (created automatically the first time someone registers)

When you run `python main.py`, you'll now see a Login/Register menu
first. You must log in successfully before the route finder menu appears.

**Note:** Passwords are stored in plain text for simplicity. This is fine
for a learning project but should never be done in a real-world app —
production systems use password hashing (e.g. bcrypt) instead.

## How to Run
1. Make sure Python is installed: `python --version`
2. From inside this folder, run:
3. `auth.py` — handles user registration and login (plain text file storage)
4. `users.txt` — stores registered usernames/passwords (auto-created)