#### Tic Tac Toe ####
# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print("-" * 13)
        print("| " + " | ".join(row) + " |")
    print("-" * 13)

import pandas as pd #import for scoreboard formatting

def scoreboard(database): #display past wins in a scoreboard
    ranking = [] #player rankings
    scores = {'Name':[], 'Score':[]} #scoreboard
    count = 0
    database = dict(sorted(database.items(), key=lambda item: item[1], reverse=True)) #rearrange player name and score by highest

    for i in database:
        scores['Name'].append(i) #add name to scoreboard
        scores['Score'].append(database[i]) #add score to scoreboard
        count += 1
        ranking.append(count) #add ranking

    print(pd.DataFrame(scores, ranking)) #Display scoreboard table

database = {}

# Function to check for a winning condition
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to get player input and update the board
def player_move(board, player):
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row in range(3) and col in range(3) and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main game function
def play_game():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        display_board(board)
        print(f"{player1} (X) vs {player2} (O)")
        print(f"{player1}'s turn" if current_player == 'X' else f"{player2}'s turn")

        player_move(board, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"{player1} wins!" if current_player == 'X' else f"{player2} wins!")
            if current_player == 'X':
                if player1 not in database:
                    database.update({player1:1}) #add new player score
                else:
                    database[player1] += 1 #update player score
            elif current_player == 'O':
                if player2 not in database:
                    database.update({player2:1}) #add new player score
                else:
                    database[player2] += 1 #update player score
            choice = input("Enter any key to continue... ")
            if choice == 'restart':
                play_game()
            elif choice == 'score':
                scoreboard(database)
            break
        
        elif is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
        
# Start the game
play_game()
