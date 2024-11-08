class Ship:
    def __init__(self, ship_type, size):
        self.ship_type = ship_type
        self.size = size
        self.coordinates = []
        self.hits = 0
        self.placed = False

    def update_coordinates(self, new_coordinates):
        self.coordinates = new_coordinates

    def register_hits(self):
        self.hits += 1

    def ship_sunk(self):
        if self.hits >= self.size:
            print(f"{self.ship_type} has Sunk")
            return True
        return False

    def check_hits(self, attack_coordinate, opponent_ships):
        for opponent_ship in opponent_ships():
            if attack_coordinate in opponent_ship.coordinates:
                opponent_ship.register_hits()
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

ships = create_ships()