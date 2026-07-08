# graph.py
# This file stores our campus map as an adjacency list.
# Each key is a location (node).
# Each value is a list of (neighbor, distance_in_meters) pairs —
# these are the places you can walk to DIRECTLY from that key,
# and how far away they are.

campus_graph = {
    "Main Gate":  [("Hostel", 60), ("Library", 250), ("Ramanujan", 70), ("APJ", 160)],
    "Hostel":     [("Parking", 90)],
    "Parking":    [("Library", 200)],
    "ATL":        [("Parking", 150)],
    "Rajaraman":  [("ATL", 100)],
    "SMV":        [("Canteen", 80), ("Rajaraman", 90)],
    "CV Raman":   [("SMV", 120)],
    "Ramanujan":  [("Library", 110), ("SMV", 130), ("CV Raman", 140)],
    "APJ":        [("CV Raman", 100)],
    "Library":    [],   # no outgoing paths from Library in the blueprint
    "Canteen":    [],   # no outgoing paths from Canteen in the blueprint
}


def get_all_locations():
    """Returns a list of every location name in the graph."""
    return list(campus_graph.keys())


def get_neighbors(location):
    """Returns the list of (neighbor, distance) pairs for a given location.
    Returns an empty list if the location doesn't exist or has no paths out."""
    return campus_graph.get(location, [])