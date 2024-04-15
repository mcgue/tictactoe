# Tic Tac Toe game as written by ChatGPT that plays against the computer
# Computer selects spot by random so play is easy for user

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def player_move(board, player):
    print_board(board)
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move! Try again.")
        else:
            board[row][col] = player
            break

def computer_move(board, player):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    row, col = random.choice(empty_cells)
    board[row][col] = player

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    turns = 0

    print("Welcome to Tic Tac Toe!")

    while turns < 9:
        player = players[current_player]
        if player == 'X':
            player_move(board, player)
        else:
            computer_move(board, player)

        if check_winner(board, player):
            print_board(board)
            if player == 'X':
                print("Congratulations! You win!")
            else:
                print("Sorry, the computer wins.")
            break

        current_player = (current_player + 1) % 2
        turns += 1

    if turns == 9:
        print_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    main()