# graph.py
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
    "Library":    [],
    "Canteen":    [],
}


def get_all_locations():
    return list(campus_graph.keys())


def get_neighbors(location):
    return campus_graph.get(location, [])