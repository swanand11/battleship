from player import Player
from computer_player import AIPlayer

def main():
    player = Player("Player 1")
    ai_player = AIPlayer()
    
    print("Place your ships:")
    player.place_ships()
    ai_player.place_ships()
    print("AI placed ships")

    player_turn = True
    game_over = False
    
    while not game_over:
        if player_turn:
            print(f"\n{player.name}'s turn to attack.")
            ai_player.board.display_board(is_ai=True)
            player.choose_attack_coordinate(ai_player.board, ai_player.ships)
            if ai_player.check_game_status():
                print("You win!")
                game_over = True
            else:
                player_turn = False
        else:
            print("\nAI's turn to attack.")
            player.board.display_board()
            ai_player.choose_attack_coordinate(player.board, player.ships)
            if player.check_game_status():
                print("AI wins!")
                game_over = True
            else:
                player_turn = True
    
    print("\nFinal Player Board:")
    player.board.display_board()
    print("\nFinal AI Board:")
    ai_player.board.display_board(is_ai=True)

if __name__ == "__main__":
    main()
