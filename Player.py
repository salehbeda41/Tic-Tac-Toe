# Player class for managing player details
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    # Method for choosing player name
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name!")

    # Method for choosing player symbol
    def choose_symbol(self):
        while True:
            symbol = input("Enter your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol!")
