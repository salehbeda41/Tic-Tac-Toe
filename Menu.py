# Menu class for displaying menus and handling user input
class Menu:
    # Method to display the main menu
    def display_main_menu(self):
        print("Welcome to Tic-Tac-Toe!")
        print("1. Start Game")
        print("2. Quit Game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice.isdigit() and choice in ["1", "2"]:
                return choice
            print("Invalid choice!")

    # Method to display the endgame menu
    def display_endgame_menu(self):
        menu_text = """\nGame Over!
1. Restart Game
2. Quit Game
Enter Your choice (1 or 2): """
        choice = input(menu_text)
        while True:
            if choice.isdigit() and choice in ["1", "2"]:
                return choice
            print("Invalid choice!")
            choice = input("Enter your choice (1 or 2): ")
