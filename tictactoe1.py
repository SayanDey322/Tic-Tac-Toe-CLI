import random

def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    player_vs_computer = choose_game_mode()
    full = isFull(board, symbol_1, symbol_2, player_vs_computer)

def intro():
    print("Hello! Welcome to Tic Tac Toe!")
    print("Rules: Player 1 (X) and Player 2 (O), or a computer, take turns marking a 3x3 grid.")
    print("Get 3 in a row to win! Let's start!")
    input("Press Enter to continue.")

def create_grid():
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def sym():
    symbol_1 = input("Player 1, do you want to be X or O? ").upper()
    symbol_2 = "O" if symbol_1 == "X" else "X"
    print(f"Player 2 will be {symbol_2}.")
    input("Press enter to continue.")
    return symbol_1, symbol_2

def choose_game_mode():
    mode = input("Do you want to play against another player or the computer? (player/computer): ").lower()
    return mode == "computer"

def startGamming(board, symbol_1, symbol_2, count, player_vs_computer):
    if count % 2 == 0:
        player = symbol_1
        print(f"Player {symbol_1}'s turn.")
        row, column = player_move(board)
    else:
        if player_vs_computer:
            print(f"Computer {symbol_2}'s turn.")
            row, column = computer_move(board, symbol_2, symbol_1)
        else:
            player = symbol_2
            print(f"Player {symbol_2}'s turn.")
            row, column = player_move(board)

    board[row][column] = symbol_1 if count % 2 == 0 else symbol_2
    return board

def player_move(board):
    row = int(input("Pick a row (0-2): "))
    column = int(input("Pick a column (0-2): "))
    
    while (row > 2 or row < 0) or (column > 2 or column < 0) or board[row][column] != " ":
        print("Invalid move. Try again.")
        row = int(input("Pick a row (0-2): "))
        column = int(input("Pick a column (0-2): "))
    
    return row, column

def computer_move(board, symbol_2, symbol_1):
    # Step 1: Check if the computer can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = symbol_2
                if is_winner(board, symbol_2):
                    return i, j
                else:
                    board[i][j] = " "
    
    # Step 2: Block the player from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = symbol_1
                if is_winner(board, symbol_1):
                    board[i][j] = " "
                    return i, j
                else:
                    board[i][j] = " "
    
    # Step 3: Pick a random empty spot
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_spots)

def isFull(board, symbol_1, symbol_2, player_vs_computer):
    count = 1
    winner = True
    while count <= 9 and winner:
        board = startGamming(board, symbol_1, symbol_2, count, player_vs_computer)
        printPretty(board)
        
        if count == 9 and winner:
            print("The board is full. It's a tie.")
        
        winner = not is_winner(board, symbol_1 if count % 2 == 0 else symbol_2)
        count += 1
    
    print("Game over.")
    report(count, winner, symbol_1, symbol_2)

def printPretty(board):
    print("---+---+---")
    for row in board:
        print(f"{row[0]}  | {row[1]} | {row[2]}")
        print("---+---+---")

def is_winner(board, symbol):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(symbol) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

def report(count, winner, symbol_1, symbol_2):
    if not winner and count % 2 == 1:
        print(f"Winner: Player {symbol_1}.")
    elif not winner and count % 2 == 0:
        print(f"Winner: Player {symbol_2}.")
    else:
        print("It's a tie!")

# Call Main
main()
