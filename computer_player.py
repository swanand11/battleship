from board import Board
from ship import ships,Ship
import random

class AIPlayer:
    def __init__(self):
        self.name = "John Doe"
        self.board = Board()
        self.ships = [ships[key] for key in ships]
        self.hits = []
        self.misses = []
        self.attack_queue = []

    def place_ships(self):
        self.board.setup_ships_ai()
    def ai_attack_coordinates(self):
        if self.attack_queue:
            return self.attack_queue.pop(0)
        else:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                attack_coordinate = (x, y)
                if attack_coordinate not in self.hits and attack_coordinate not in self.misses:
                    return attack_coordinate

    def choose_attack_coordinate(self):
        print(f"Misses: {self.misses}")
        print(f"Hits: {self.hits}")
        attack_coordinates = self.ai_attack_coordinates()
        print(f"AI attacking: {attack_coordinates}")
        hit = False
        for ship in self.ships:
            if ship.check_hits(attack_coordinates):
                print(f"Hit on {ship.ship_type} at {attack_coordinates}!")
                self.hits.append(attack_coordinates)  
                hit = True
                self.board.register_hit_board(attack_coordinates[1],attack_coordinates[0])
                self.search_adjacent_cells(attack_coordinates)  
                break

        if not hit:
            print(f"Miss at {attack_coordinates}!")
            self.misses.append(attack_coordinates)  
            self.board.misses_hit_board_ai(attack_coordinates[1],attack_coordinates[0])

    def search_adjacent_cells(self, last_hit):
        x, y = last_hit
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 10 and 0 <= new_y < 10: 
                attack_coordinate = (new_x, new_y)
                if attack_coordinate not in self.hits and attack_coordinate not in self.misses:
                    print(f"Adding adjacent attack to queue: {attack_coordinate}")
                    self.attack_queue.append(attack_coordinate)

    def check_game_status(self):

        for ship in self.ships:
            if not ship.ship_sunk():
                return False
        return True  


if __name__ == "__main__":
    aiplayer = AIPlayer()
    aiplayer.place_ships()
    n=0
    while n<5:
        n+=1
        aiplayer.board.display_board()
        aiplayer.choose_attack_coordinate()
        for key, ship in ships.items():
            print(f"{ship.ship_type} hits: {ship.hits}")
