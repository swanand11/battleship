import numpy as np
from ship import ships
import random
class Board:
    def __init__(self):
        self.play_arena1 = np.zeros((10, 10))  
        self.play_arena2 = np.zeros((10, 10))  

    def display_board(self):
        print(self.play_arena2)

    def validate_coordinates(self, x, y, ship_size, direction):
        if direction == 1:  
            if x < 0 or x > 9 or x + ship_size > 10:
                return False
            for col in range(x, x + ship_size):
                if self.play_arena2[y, col] != 0:  
                    return False
        elif direction == 2:  
            if y < 0 or y > 9 or y + ship_size > 10:
                return False
            for row in range(y, y + ship_size):
                if self.play_arena2[row, x] != 0:  
                    return False
        return True

    def validate_coordinates_ai(self, x, y, ship_size, direction):
        if direction == 1:  
            if x < 0 or x > 9 or x + ship_size > 10:
                return False
            for col in range(x, x + ship_size):
                if self.play_arena1[y, col] != 0:  
                    return False
        elif direction == 2:  
            if y < 0 or y > 9 or y + ship_size > 10:
                return False
            for row in range(y, y + ship_size):
                if self.play_arena1[row, x] != 0:  
                    return False
        return True

    def place_on_board(self, x, y, ship_size, direction):
        if direction == 1:  
            for col in range(x, x + ship_size):
                self.play_arena2[y, col] = 1  
        elif direction == 2:  
            for row in range(y, y + ship_size):
                self.play_arena2[row, x] = 1 

    def list_of_coordinates(self, x, y, ship, direction):
        ship.coordinates.clear()  
        if direction == 1:  
            for col in range(x, x + ship.size):
                ship.coordinates.append([y, col])  
        elif direction == 2:  
            for row in range(y, y + ship.size):
                ship.coordinates.append([row, x])  

    def register_hit_board(self, x, y):
        self.play_arena2[y, x] = 2  

    def misses_hit_board(self, x, y):
        self.play_arena2[y, x] = -1  

    def register_hit_board_ai(self, x, y):
        self.play_arena1[y, x] = 2  

    def misses_hit_board_ai(self, x, y):
        self.play_arena1[y, x] = -1  

    def setup_ships(self):
        ships_placed_count = 0
        while ships_placed_count < len(ships):
            print("Select your ship to place (only one of each type can be placed):")
            for key, ship in ships.items():
                if not ship.placed:  
                    print(f"Press ({key}) for {ship.ship_type} (size {ship.size})")

            ship_type = input("Choose a ship: ")
            if ship_type not in ships:
                print("Invalid selection. Please try again.")
                continue
            selected_ship = ships[ship_type]
            
            if selected_ship.placed:
                print("Ship already placed. Please select a different ship.")
                continue
            
            direction = input("Press (1) for placing horizontally\nPress (2) for placing vertically\n")
            if direction not in ["1", "2"]:
                print("Invalid direction selection. Please try again.")
                continue
            try:
                x = int(input("Please enter start x coordinate: "))
                y = int(input("Please enter start y coordinate: "))
            except ValueError:
                print("Invalid input! Please enter numeric values for coordinates.")
                continue
            if not (0 <= x <= 9) or not (0 <= y <= 9):
                print("Coordinates out of bounds! Please enter values between 0 and 9.")
                continue
            if self.validate_coordinates(x, y, selected_ship.size, int(direction)):
                self.place_on_board(x, y, selected_ship.size, int(direction))
                self.list_of_coordinates(x, y, selected_ship, int(direction))
                selected_ship.placed = True
                ships_placed_count += 1
                print(f"{selected_ship.ship_type} placed successfully!")
            else:
                print("Invalid placement! Please try again.")
    def setup_ships_ai(self):
        ships_placed_count = 0  
        while ships_placed_count < len(ships):
            ship_keys = list(ships.keys())  
            ship_type = random.choice(ship_keys)  
            selected_ship = ships[ship_type]
            if selected_ship.placed:
                continue
            direction = random.choice([1, 2])
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.validate_coordinates(x, y, selected_ship.size, direction):
                self.place_on_board(x, y, selected_ship.size, direction)
                self.list_of_coordinates(x, y, selected_ship, direction)
                selected_ship.placed = True  
                ships_placed_count += 1
                print(f"{selected_ship.ship_type} placed successfully!")
            else:
                print(f"Invalid placement for {selected_ship.ship_type}. Retrying...")


