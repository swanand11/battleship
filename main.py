from board import Board 
from ship import ships   
if __name__=="__main__":
    board=Board()
    print("Welcome to the Battleship game!")
    board.setup_ships()
    print("\nAll ships have been placed.\n")
    print("Final Board Configuration:")
    board.display_board()
    for key, ship in ships.items():
        print(f"{ship.ship_type} coordinates: {ship.coordinates}")
