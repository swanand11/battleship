from board import Board
from ship import ships

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.ships = [ships[key] for key in ships]
        self.hits = []
        self.misses = []
    def place_ships(self):
        print(f"{self.name}, it's time to place your ships!")
        self.board.setup_ships()
    def choose_attack_coordinate(self):
        print("Misses -->", self.misses)
        print("Hits -->", self.hits)
        try:
            x = int(input("Please enter x coordinate for the attack: "))
            y = int(input("Please enter y coordinate for the attack: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for coordinates.")
            return
        if not (0 <= x <= 9) or not (0 <= y <= 9):
            print("Coordinates out of bounds! Please enter values between 0 and 9.")
            return
        attack_coordinates = [y, x]
        hit = False
        for ship in self.ships:
            if ship.check_hits(attack_coordinates):
                print(f"Hit on {ship.ship_type}!")
                self.hits.append(attack_coordinates)
                hit = True
                break 

        if not hit:
            print("Miss!")
            self.misses.append(attack_coordinates)

if __name__ == "__main__":
    player = Player("abc")
    player.place_ships()
    Board.display_board()
    player.choose_attack_coordinate()
    for key, ship in ships.items():
        print(f"{ship.ship_type} hits: {ship.hits}")  
