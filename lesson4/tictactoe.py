'''
_1_|_2_|_3_
_4_|_5_|_6_   
 7 | 8 | 9


___|___|_O_
___|_O_|_X_   
   |   |

tictactoe_list = [["", "", "O"],
                  ["", "O", "X"],
                  ["",  "", ""]]

three in a row
horizontal
for every row in tictactoe_list
    everything has to be equal

vertical
for every column in tictactoe_list
    everything has to be equal

diagonal
0th index, 1st index, 2nd index
or
2nd index, 1st index, 0th index

when does the end
someone wins
have three in a row
tie - runs out of spaces in the board

'''

'''
input: list - tictactoe_list 
output: string - tictactoe board
'''
def render_board(tictactoe_list):
    row_string = ""
    for row in tictactoe_list:
        pass
    
    return row_string

'''
input: list - tictactoe_list
output: boolean - win/lose
'''
def win_vertical(tictactoe_list):
    for i in range(3):
        if (tictactoe_list[0][i] == tictactoe_list[1][i]) and (tictactoe_list[1][i] == tictactoe_list[2][i]) and tictactoe_list[0][i] != "":
            return True
    return False  

'''
input: list - tictactoe_list
output: boolean - win/lose
'''
def win_horizontal(tictactoe_list):
    for row in tictactoe_list:
        # fix this by changing rows to not just test if empty string is equal to empty string
        if (row[0] == row[1]) and (row[1] == row[2]) and row[0] != "":
            return True
    return False

'''
input: list - tictactoe_list
output: boolean - win/lose
'''
def win_diagonal(tictactoe_list):
    if (tictactoe_list[0][0] == tictactoe_list[1][1]) and (tictactoe_list[1][1] == tictactoe_list[2][2]) and tictactoe_list[0][0]!= "":
        return True
    if (tictactoe_list[0][2] == tictactoe_list[1][1]) and (tictactoe_list[1][1] == tictactoe_list[2][0]) and tictactoe_list[0][2]!= "":
        return True
    return False

def game_results(board):
    total_pieces = 0
    for row in board:
        for eachItem in row:
            if eachItem != "":
                total_pieces += 1

    if win_vertical(board) or win_diagonal(board) or win_horizontal(board):
        return "Win"
    elif total_pieces == 9:
        return "Tie"
    else:
        return "Continue"

'''
input: board list, integer from 1-9
output: list board
'''
def place_num_on_board(board, pos, piece):
    new_board = board
    if pos == "1":
        new_board[0][0] = piece
    elif pos == "2":
        new_board[0][1] = piece
    elif pos == "3":
        new_board[0][2] = piece
    elif pos == "4":
        new_board[1][0] = piece
    elif pos == "5":
        new_board[1][1] = piece
    elif pos == "6":
        new_board[1][2] = piece
    elif pos == "7":
        new_board[2][0] = piece
    elif pos == "8":
        new_board[2][1] = piece
    else:
        new_board[2][2] = piece
    return new_board

def print_number_board():
    print("_1_|_2_|_3_")
    print("_4_|_5_|_6_")
    print("_7_|_8_|_9_")

def check_input_valid(pos):
    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if pos not in positions:
        return False
    return True

def tictactoe():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    while True:
        print_number_board()
        player1_move = input("Player1 (X) select a position from 1-9: ")

        if not check_input_valid(player1_move):
            player1_move = input("INVALID INPUT! \n Player1 (X) select another position from 1-9: ")

        board = place_num_on_board(board, player1_move, "X")
        print(board)
        result = game_results(board)
        if result == "Win":
            print("Player1 Wins!")
            break
        elif result == "Tie":
            print("You tied!")
            break

        player2_move = input("Player2 (O) select a position from 1-9: ")

        if not check_input_valid(player2_move):
            player2_move = input("INVALID INPUT! \n Player2 (O) select another position from 1-9: ")

        board = place_num_on_board(board, player2_move, "O")
        print(board)
        result = game_results(board)
        if result == "Win":
            print("Player2 Wins!")
            break
        elif result == "Tie":
            print("You tied!")
            break


        print("\n=============== \n")

if __name__ == "__main__":
    tictactoe()