class Ship:
    def __init__(self,ship_type,size):
        self.ship_type=ship_type
        self.size=size
        self.coordinates=[]
        self.hits=0
        self.placed = False
    def update_coordinates(self,new_coordinates):
        self.coordinates = new_coordinates
    def register_hits(self):
        self.hits+=1
    def ship_sunk(self):
        if self.hits>=self.size:
            print(self.ship_type," has Sunk")
            return True
        return False
    def check_hits(self,attack_coordinate):
        if not self.coordinates:
            print(f"Error: Coordinates for {self.ship_type} are not set")
            return False
        if attack_coordinate in self.coordinates:
            self.register_hits()
            return True
        return False
    def print_coordinates(self):
        print(self.coordinates)
carrier = Ship("Carrier", 5)
battleship = Ship("Battleship", 4)
destroyer = Ship("Destroyer", 3)
submarine = Ship("Submarine", 3)
patrol_boat = Ship("Patrol Boat", 2)
ships = {
    "1": carrier,
    "2": battleship,
    "3": destroyer,
    "4": submarine,
    "5": patrol_boat,
}
