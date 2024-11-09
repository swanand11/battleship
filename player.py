from board import Board
from ship import create_ships

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.ships = create_ships()
        self.hits = []
        self.misses = []

    def place_ships(self):
        print(f"{self.name}, place your ships.")
        self.board.setup_ships(self.ships)

    def choose_attack_coordinate(self, opponent_board, opponent_ships):
        try:
            x, y = int(input("Enter x: ")), int(input("Enter y: "))
        except ValueError:
            print("Coordinates must be integers!")
            return False

        hit = False
        for ship in opponent_ships.values():
            if [y, x] in ship.coordinates:
                print(f"Hit on {ship.ship_type}!")
                ship.register_hit((x,y))
                self.hits.append([x, y])
                opponent_board.register_hit_or_miss(x, y, is_ai=True, hit=True)
                if ship.ship_sunk():
                    print(f"{ship.ship_type} has sunk!")
                hit = True
                break

        if not hit:
            print("Miss!")
            self.misses.append([x, y])
            opponent_board.register_hit_or_miss(x, y, is_ai=True, hit=False)

    def check_game_status(self):
        return all(ship.ship_sunk() for ship in self.ships.values())
