class Ship:
    def __init__(self, ship_type, size):
        self.ship_type = ship_type
        self.size = size
        self.coordinates = []  
        self.hit_coordinates = set()  
        self.placed = False

    def update_coordinates(self, new_coordinates):
        self.coordinates = new_coordinates

    def register_hit(self, coordinate):
        coord_tuple = tuple(coordinate) if isinstance(coordinate, list) else coordinate
        if coord_tuple not in self.hit_coordinates:
            self.hit_coordinates.add(coord_tuple)

    def ship_sunk(self):
        if len(self.hit_coordinates) >= self.size:
            return True
        return False

    def print_coordinates(self):
        print(self.coordinates)

def create_ships():
    return {
        "1": Ship("Carrier", 5),
        "2": Ship("Battleship", 4),
        "3": Ship("Destroyer", 3),
        "4": Ship("Submarine", 3),
        "5": Ship("Patrol Boat", 2),
    }