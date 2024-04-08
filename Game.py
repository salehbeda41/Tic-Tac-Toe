import os
from Player import *
from Board import *
from Menu import *
# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")





# Game class for managing the game flow
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.current_player_index = 0
    
    # Method to start the game
    def start_game(self):
        choice = self.menu.display_main_menu()
        clear_screen()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    # Method to setup players before the game
    def setup_players(self):
        while True:
            for number, player in enumerate(self.players, start=1):
                print(f"Player {number}:")
                player.choose_name()
                player.choose_symbol()
                clear_screen()
            if self.players[0].symbol == self.players[1].symbol:
                print("Invalid Symbols! (Should be different)")
            else:
                break
    
    # Method to play the game
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                clear_screen()
                self.board.display_board()
                if self.check_win():
                    print(f"Winner: {self.players[1 - self.current_player_index].name} ({self.players[1 - self.current_player_index].symbol})")
                if self.check_draw():
                    print("Draw!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            clear_screen()
    
    # Method to play a single turn
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a (number) between 1-9")
        self.switch_player()
    
    # Method to switch players after each turn
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    
    # Method to check if there is a winner
    def check_win(self):
        win_combination = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for comb in win_combination:
            if self.board.board[comb[0]] == self.board.board[comb[1]] == self.board.board[comb[2]]:
                return True
        return False
    
    # Method to check if the game ended in a draw
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) and not self.check_win()
    
    # Method to restart the game
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
    
    # Method to quit the game
    def quit_game(self):
        clear_screen()
        print("\n\t\tThank you, See you soon...")

# Main entry point of the program
if __name__ == "__main__":
    game = Game()
    game.start_game()
