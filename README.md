# Campus Route Finder

A command-line tool that finds the shortest route between locations on a
campus, using graph algorithms: BFS, Dijkstra's Algorithm, and DFS. Includes
a simple login system and per-user route history.

## Project Structure
- `graph.py` — stores the campus map as an adjacency list
- `bfs.py` — finds the route with the fewest stops (unweighted shortest path)
- `dijkstra.py` — finds the route with the shortest total distance (weighted shortest path)
- `dfs.py` — finds all possible routes between two points, and checks for disconnected locations
- `auth.py` — handles user registration and login (plain text file storage, with password validation)
- `history.py` — saves, retrieves, and clears each user's past route searches
- `main.py` — the interactive menu that ties everything together
- `test_routes.py` — automated tests comparing BFS vs Dijkstra, and a stress test

## How to Run
1. Make sure Python is installed: `python --version`
2. From inside this folder, run:
3. Register a new account (or log in if you already have one).
4. Choose an option from the menu and enter location names exactly as listed.

## Login / Registration (Extra Addition)
As an addition on top of the core roadmap project, a username/password
login system was added using `auth.py`. This is a beginner-level,
file-based system — not intended for real-world security use.

- `auth.py` — handles registering new users and logging in
- `users.txt` — stores registered usernames and passwords as plain text
  (created automatically the first time someone registers)
- Registration requires a password at least 6 characters long, and asks
  for password confirmation to catch typos.
- A **Logout** option returns to the Login/Register screen without
  closing the program, so a different user can log in without restarting.

**Note:** Passwords are stored in plain text for simplicity. This is fine
for a learning project but should never be done in a real-world app —
production systems use password hashing (e.g. bcrypt) instead.

## Route History (Extra Addition)
Each logged-in user's searched routes (BFS and Dijkstra only) are saved
to `history.txt`, tagged with their username, and kept separate from
other users' history.

- **View my route history** — lists all of your past searches
- **Clear my route history** — deletes only your own history entries,
  after a yes/no confirmation, leaving other users' history untouched

## Main Menu Options
1. Find shortest route by stops (BFS)
2. Find shortest route by distance (Dijkstra)
3. Show all possible routes (DFS)
4. Check for disconnected locations
5. Find route while avoiding a location
6. List all locations reachable from a point
7. View my route history
8. Clear my route history
9. Logout
10. Exit program

## Running Tests
This prints a comparison table of BFS vs Dijkstra results, and confirms every
route in the campus map can be processed without errors.

## Sample Test Cases
| Start      | End      | BFS Path                              | Dijkstra Path                          |
|------------|----------|----------------------------------------|-----------------------------------------|
| Main Gate  | Canteen  | Main Gate -> Ramanujan -> SMV -> Canteen | Main Gate -> Ramanujan -> SMV -> Canteen |
| Canteen    | Main Gate| No path (edges are one-way)            | No path (edges are one-way)             |
| Library    | Main Gate| No path (Library has no outgoing edges)| No path                                 |

## BFS vs Dijkstra — Key Difference
- **BFS** treats every path as equal length — it only counts the number of
  stops. It's faster to reason about but ignores real-world distance.
- **Dijkstra's Algorithm** accounts for actual distances (meters), always
  expanding the closest known location next using a min-heap priority
  queue. This gives the truly shortest route by distance, which may have
  *more* stops than the BFS answer if a longer chain of short hops beats a
  few long hops.

## Complexity
- BFS: O(V + E) — visits every location (V) and path (E) at most once.
- Dijkstra (with a min-heap): O((V + E) log V) — the log V factor comes
  from maintaining the priority queue.
- DFS (all paths): exponential in the worst case, since it explores every
  possible route rather than stopping at the first/shortest one.