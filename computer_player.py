from board import Board
from ship import create_ships
import random

class AIPlayer:
    def __init__(self):
        self.name = "AI"
        self.board = Board()
        self.ships = create_ships()
        self.hits = set()  # Using set for faster lookup
        self.misses = set()  # Using set for faster lookup
        self.attack_queue = []
        self.previous_attacks = set()  # Track all previous attacks

    def place_ships(self):
        self.board.setup_ships_ai(self.ships)

    def is_valid_attack(self, x, y):
        return (0 <= x <= 9 and 0 <= y <= 9 and 
                (x, y) not in self.previous_attacks)

    def ai_attack_coordinates(self):
        # First try coordinates from the queue
        while self.attack_queue:
            x, y = self.attack_queue.pop(0)
            if self.is_valid_attack(x, y):
                return [x, y]
        
        # If queue is empty or all queued coordinates are invalid, try random coordinates
        attempts = 0
        while attempts < 100:  # Prevent infinite loop
            x, y = random.randint(0, 9), random.randint(0, 9)
            if self.is_valid_attack(x, y):
                return [x, y]
            attempts += 1
        
        # If no valid moves found, return None
        return None

    def search_adjacent_cells(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_attack(new_x, new_y):
                self.attack_queue.append((new_x, new_y))

    def choose_attack_coordinate(self, opponent_board, opponent_ships):
        coordinates = self.ai_attack_coordinates()
        if not coordinates:
            print("AI has no valid moves left!")
            return

        x, y = coordinates
        print(f"AI attacking ({x}, {y})")
        hit = False
        self.previous_attacks.add((x, y))
        attack_coord = (y, x)  

        for ship in opponent_ships.values():
            if attack_coord in {tuple(coord) for coord in ship.coordinates}:
                if attack_coord not in ship.hit_coordinates:
                    print(f"AI hit on {ship.ship_type}!")
                    ship.register_hit(attack_coord)
                    self.hits.add((x, y))
                    opponent_board.register_hit_or_miss(x, y, hit=True)
                    self.search_adjacent_cells(x, y)
                    hit = True
                    if ship.ship_sunk():
                        print(f"{ship.ship_type} has sunk!")
                    break

        if not hit:
            print(f"AI missed at ({x}, {y})")
            self.misses.add((x, y))
            opponent_board.register_hit_or_miss(x, y, hit=False)

    def check_game_status(self):
        return all(ship.ship_sunk() for ship in self.ships.values())