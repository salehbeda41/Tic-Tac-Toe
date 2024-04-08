# Board class for managing the game board
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    # Method to display the game board
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)
    
    # Method to update the game board with player's move
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    # Method to check if the move is valid
    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    # Method to reset the game board
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]