from board import Board
from ship import create_ships
import random

class AIPlayer:
    def __init__(self):
        self.name = "AI"
        self.board = Board()
        self.ships = create_ships()
        self.hits = []
        self.misses = []
        self.attack_queue = []

    def place_ships(self):
        self.board.setup_ships_ai(self.ships)

    def ai_attack_coordinates(self):
        if self.attack_queue:
            return self.attack_queue.pop(0)
        while True:
            x, y = random.randint(0, 9), random.randint(0, 9)
            if [x, y] not in self.hits and [x, y] not in self.misses:
                return [x, y]

    def choose_attack_coordinate(self, opponent_board, opponent_ships):
        x, y = self.ai_attack_coordinates()
        print(f"AI attacking ({x}, {y})")
        hit = False

        for ship in opponent_ships.values():
            if [y, x] in ship.coordinates:
                print(f"AI hit on {ship.ship_type}!")
                ship.register_hits()
                self.hits.append([x, y])
                opponent_board.register_hit_or_miss(x, y, hit=True)
                hit = True
                if ship.ship_sunk():
                    print(f"{ship.ship_type} has sunk!")
                break

        if not hit:
            print(f"AI missed at ({x}, {y})")
            self.misses.append([x, y])
            opponent_board.register_hit_or_miss(x, y, hit=False)
    def check_game_status(self):
        return all(ship.ship_sunk() for ship in self.ships.values())