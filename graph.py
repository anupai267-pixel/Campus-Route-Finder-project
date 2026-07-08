# graph.py
campus_graph = {
    "Main Gate":  [("Hostel", 60), ("Library", 250), ("Ramanujan", 70), ("APJ", 160)],
    "Hostel":     [("Parking", 90),("Library", 80), ("Main Gate", 60)],
    "Parking":    [("Library", 200), ("ATL", 150), ("Hostel", 90)],
    "ATL":        [("Parking", 150), ("Rajaraman", 100)],
    "Rajaraman":  [("ATL", 100), ("Canteen", 50), ("Library", 130), ("SMV", 90)],
    "SMV":        [("Canteen", 80), ("Rajaraman", 90), ("Ramanujan", 130), ("CV Raman", 120)],
    "CV Raman":   [("SMV", 120), ("APJ", 100)],
    "Ramanujan":  [("Library", 110), ("SMV", 130), ("APJ", 40), ("Main Gate", 70)],
    "APJ":        [("CV Raman", 100), ("Ramanujan", 40), ("Main Gate", 160)],
    "Library":    [("Rajaraman",130), ("Parking", 200), ("Hostel", 80), ("Main Gate", 250),("Ramanujan", 110)],
    "Canteen":    [("Rajaraman", 50), ("SMV", 80)],
}


def get_all_locations():
    return list(campus_graph.keys())


def get_neighbors(location):
    return campus_graph.get(location, [])