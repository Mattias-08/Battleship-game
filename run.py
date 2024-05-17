import random
from colorama import Fore, Back, Style


board = [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Prints the board with row numbers and labels."""
    print("    A   B   C")
    for i, row in enumerate(board, start=1):
        print(f"{i}  ", end="")  # Add row number with a space
        for cell in row:
            if cell == 'X':
                print(f"[{Fore.RED}{cell}{Style.RESET_ALL}]", end=" ")  # Red for X
            elif cell == 'O':
                print(f"[{Fore.BLUE}{cell}{Style.RESET_ALL}]", end=" ")  # Blue for O
            else:
                print(f"[ ]", end=" ")  # Default for empty cells
        print(f"{Style.RESET_ALL}")  # Reset formatting and add newline

def choose_and_update_cell(board, player):
    """Prompts the player to choose a cell and updates the board."""
    while True:
        cell = input(f"Player's turn: ").strip().lower()
        if len(cell) == 2 and cell[0] in 'abc' and cell[1] in '123':
            row = int(cell[1]) - 1
            col = ord(cell[0]) - ord('a')
            if board[row][col] == ' ':
                board[row][col] = player
                return  # Exit the loop after successful placement
            else:
                print(f"""{Fore.RED}
                Cell already occupied. Please choose another one.
                {Style.RESET_ALL}""")
        else:
            print(
                f"""{Fore.RED} 
Invalid input. Please enter a letter (A-C) and a number (1-3).
{Style.RESET_ALL}"""
            )


def is_valid_move(board, row, col):
    """Checks if the specified move is valid (cell is empty)."""
    return board[row][col] == ' '


def computer_move(board):
    """Generates a random valid move for the computer."""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if is_valid_move(board, row, col):
            return row, col


def check_winner(board, player):
    """Checks if the specified player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def go_back_start():
    print("Lets play again!")
    update_the_board()
    main_logic()

def welcome_message():
    print(f"""
                            Welcome to 3 in a Row!
Rules:
- Players take turns placing their mark (X or O) on the board.
- The board is represented by letters (A-C) for columns 
and numbers (1-3) for rows.
- Input your letter then your number (e.g., A1) 
in order to place your mark.
""")


def main_logic():
    current_player = 'X'  # Start with player 
    
    while True:
        display_board(board)  # calling the boardfunction

        # Player's turn
        if current_player == 'X':
            print("debug current_player")
            choose_and_update_cell(board, current_player)  # Pass the board

        # Computer's turn
        elif current_player == 'O':
            print(f"Computer's turn:")
            row, col = computer_move(board)  # Pass the board
            board[row][col] = current_player 
        
        # Check for a winner
        if check_winner(board, current_player):
            display_board(board)
            if current_player == 'X':
                print(f"{Fore.GREEN}You Win!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Computer Wins!{Style.RESET_ALL}")
            go_back_start()
            break
        
        # Check for a draw
        if all(cell != ' ' for row in board for cell in row):
            display_board(board)
            print(f"{Fore.YELLOW}It's a draw!{Style.RESET_ALL}")
            go_back_start()
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

def main():
    """Main game loop."""
    welcome_message()
    main_logic()
    


if __name__ == "__main__":
    main()