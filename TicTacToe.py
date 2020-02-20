# Global Variables

# If game is still going
game_still_running = True

# Who won? Or Tie?
winner = None

# Who's turn is it?
current_player = "X"

# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play the game
def play_game():
    # display the game board
    display_board()

    # While the game is still running
    while game_still_running:
        # handle single turn of player
        handle_turn(current_player)

        # Check if game has ended
        check_if_game_over()

        # Flip players per turn
        flip_player()

    #       The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("It's a tie! You both suck!")


# Handle Turn
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1 - 9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 - 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there! Go again!")

    board[position] = player
    display_board()


# Check if game is finished
def check_if_game_over():
    check_if_win()
    check_if_tie()


# Check Win
def check_if_win():
    # Setup Global variables
    global winner

    #    Check Rows
    row_winner  = check_row()
    #    Check Columns
    column_winner = check_columns()
    #    Check Diagonals
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return

def check_row():
    # Set global variables
    global game_still_running

    # Check if rows have equal values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # if any row has a match, flag the win
    if row_1 or row_2 or row_3:
        game_still_running = False
    #     Return the winner
    if row_1:
       return board[0]
    elif row_2:
       return board[3]
    elif row_3:
       return board[6]
    return


def check_columns():
    # Set global variables
    global game_still_running

    # Check if columns have equal values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # if any row has a match, flag the win
    if column_1 or column_2 or column_3:
        game_still_running = False
    #     Return the winner
    if column_1:
       return board[0]
    elif column_2:
       return board[2]
    elif column_3:
       return board[2]
    return
    return


def check_diag():
    # Set global variables
    global game_still_running

    # Check if diags have equal values
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"

    # if any diag has a match, flag the win
    if diag_1 or diag_2:
        game_still_running = False
    #     Return the winner
    if diag_1:
       return board[0]
    elif diag_2:
       return board[6]
    return
    return


# Check Tie
def check_if_tie():
    global board
    global game_still_running

    if "-" not in board:
        game_still_running = False
    return


# Flip player
def flip_player():
    # Set Global Variables
    global current_player

    # If current player is X, switch to O after the turn is over
    if current_player == "X":
        current_player = "O"
    # If current player is X, switch to O after the turn is over
    elif current_player == "O":
        current_player = "X"
    return


play_game()
