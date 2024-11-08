import numpy as np
import random
from ship import Ship, create_ships

class Board:
    def __init__(self):
        # Initialize two boards: one for the player, one for the AI
        self.play_arena1 = np.zeros((10, 10))  # player board
        self.play_arena2 = np.zeros((10, 10))  # AI board

    def display_board(self, is_ai=False):
        """
        Display the current state of the board. AI's board hides ship locations.
        """
        board = self.play_arena2 if is_ai else self.play_arena1
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(10):
            row = f"{i} "
            for j in range(10):
                value = board[i][j]
                if value == 0:
                    row += ". "
                elif value == 1:
                    row += "S " if not is_ai else ". "  # Hide AI ships
                elif value == 2:
                    row += "H "  # Hit
                elif value == -1:
                    row += "M "  # Miss
            print(row)

    def validate_coordinates(self, x, y, ship_size, direction, is_ai=False):
        """
        Check if the ship can be placed at the given coordinates without overlapping
        or going out of bounds. Adjusts checks based on direction.
        """
        arena = self.play_arena2 if is_ai else self.play_arena1
        if direction == 1:  # horizontal placement
            if x + ship_size > 10:
                return False
            return all(arena[y][col] == 0 for col in range(x, x + ship_size))
        elif direction == 2:  # vertical placement
            if y + ship_size > 10:
                return False
            return all(arena[row][x] == 0 for row in range(y, y + ship_size))

    def place_on_board(self, x, y, ship, direction, is_ai=False):
        """
        Place a ship on the board and update the ship's coordinates. Horizontal or vertical.
        """
        arena = self.play_arena2 if is_ai else self.play_arena1
        ship_coordinates = []

        if direction == 1:  # horizontal
            for col in range(x, x + ship.size):
                arena[y][col] = 1
                ship_coordinates.append([y, col])
        elif direction == 2:  # vertical
            for row in range(y, y + ship.size):
                arena[row][x] = 1
                ship_coordinates.append([row, x])

        # Update the ship's coordinates for tracking
        ship.update_coordinates(ship_coordinates)
        ship.placed = True

    def register_hit_or_miss(self, x, y, is_ai=False, hit=False):
        """
        Mark a cell as hit or miss. AI or player board is updated based on 'is_ai' flag.
        """
        arena = self.play_arena2 if is_ai else self.play_arena1
        arena[y][x] = 2 if hit else -1  # 2 for hit, -1 for miss

    def setup_ships(self, ships):
        """
        Place ships for the player with manual input for each ship. Ensures valid placement.
        """
        ships_placed_count = 0
        while ships_placed_count < len(ships):
            print("\nCurrent board state:")
            self.display_board()
            
            print("\nSelect a ship to place (only one of each type):")
            for key, ship in ships.items():
                if not ship.placed:
                    print(f"Press ({key}) for {ship.ship_type} (size {ship.size})")
            
            ship_type = input("Choose a ship: ")
            if ship_type not in ships:
                print("Invalid selection. Try again.")
                continue
            
            selected_ship = ships[ship_type]
            if selected_ship.placed:
                print("Ship already placed. Choose another.")
                continue

            direction = input("Press (1) for horizontal or (2) for vertical placement: ")
            if direction not in ["1", "2"]:
                print("Invalid direction. Try again.")
                continue

            try:
                x = int(input("Enter starting x-coordinate (0-9): "))
                y = int(input("Enter starting y-coordinate (0-9): "))
            except ValueError:
                print("Invalid input! Enter numbers for coordinates.")
                continue

            if not (0 <= x <= 9) or not (0 <= y <= 9):
                print("Coordinates out of bounds! Enter values between 0 and 9.")
                continue

            if self.validate_coordinates(x, y, selected_ship.size, int(direction)):
                self.place_on_board(x, y, selected_ship, int(direction))
                ships_placed_count += 1
                print(f"{selected_ship.ship_type} placed successfully!")
            else:
                print("Invalid placement! Ships cannot overlap or extend beyond the board.")

    def setup_ships_ai(self, ships):
        """
        Automatically place AI ships randomly on the board. Ensures valid placement.
        """
        attempts, max_attempts = 0, 1000
        ships_placed_count = 0
        
        while ships_placed_count < len(ships) and attempts < max_attempts:
            attempts += 1
            available_ships = [ship for ship in ships.values() if not ship.placed]
            if not available_ships:
                break

            ship = random.choice(available_ships)
            direction = random.randint(1, 2)
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            if self.validate_coordinates(x, y, ship.size, direction, is_ai=True):
                self.place_on_board(x, y, ship, direction, is_ai=True)
                ships_placed_count += 1
        
        if attempts >= max_attempts:
            print("Error: Could not place all AI ships within limit. Restart the game.")
            return False
        return True
