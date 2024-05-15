import random

def display_board(board):
    """Displays the current state of the game board."""
    print("   | A | B | C ")
    print("---+---+---")
    for row in board:
        print(f" {row.index(1)+1} | {' | '.join(row)} ")
    print("---+---+---")

def choose_and_update_cell(board, player):
    """Prompts the player to choose a cell and updates the board."""
    while True:
        cell = input(f"Player {player}'s turn (e.g., A1): ").strip().lower()
        if len(cell) == 2 and cell[0] in 'abc' and cell[1] in '123':
            row = int(cell[1]) - 1
            col = ord(cell[0]) - ord('a')
            if board[row][col] == ' ':
                board[row][col] = player
                return  # Exit the loop after successful placement
            else:
                print("Cell already occupied. Please choose another one.")
        else:
            print("Invalid input. Please enter a letter (A-C) and a number (1-3).")

def is_valid_move(board, row, col):
    """Checks if the specified move is valid (cell is empty)."""
    return board[row][col] == ' '