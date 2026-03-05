'''
# Project Creation Date: 12:43:59 PM, 3/04/2026
'''

board = ["_"] * 42

rows = [list(range(i, i + 7)) for i in range(0, 42, 7)]   
columns = [list(range(i, 42, 7)) for i in range(7)]
diagonals_6 = [
    #top right to bottom left
    [x for x in range(3, 22, 6)],
    [x for x in range(4, 29, 6)],
    [x for x in range(5, 36, 6)],
    [x for x in range(6, 37, 6)],
    [x for x in range(13, 38, 6)],
    [x for x in range(20, 39, 6)]
]

diagonals_8 = [
    #top left to bottom right
    [x for x in range(3, 28, 8)],
    [x for x in range(2, 35, 8)],
    [x for x in range(1, 42, 8)],
    [x for x in range(0, 41, 8)],
    [x for x in range(7, 40, 8)],
    [x for x in range(14, 39, 8)]
]

red_first = ["red"[:x+1] for x in range(len("red"))]
yellow_first = ["yellow"[:x+1] for x in range(len("yellow"))]
text_colors = {
    1: '\033[31m',  #Red
    2: '\033[33m',  #Yellow
    3: '\033[1m',   #Bold
    4: "\033[0m"    #Reset
}
player_repr = {
    'Yellow': '\033[33m', 
    text_colors[2] + "Yellow": '\033[33m', 
    'Red': '\033[31m',
    text_colors[1] + "Red": '\033[31m'
}
col = 0 #Marks the current text color for text_colors

def decide_first_player():
    while True:
        first = input(text_colors[4] + "Who is going first? Yellow or Red?\n>").lower()
        if first in yellow_first:
            current_player = text_colors[2] + "Yellow"
            col = 2
        elif first in red_first:
            current_player = text_colors[1] + "Red"
            col = 1
        else:
            print("Invalid")
            continue
        
        return col, current_player
def print_board():
    for row in range(0, 42, 7):
        print(" ".join(board[row:row+7]))
def validate(user_move):
    if board[user_move-1] != "_":
        return False
    else:
        return True
def user_makes_move(col, current_player):
    while True:
        user_move = input(f"{text_colors[col]}{current_player}'s {text_colors[4]}move.\nWhich column?\n>")
        
        if user_move in [str(x+1) for x in range(7)]:
            if not validate(int(user_move)):
                print("That row is fully occupied.")
                continue
            else:
                return int(user_move)
        else:
            print("Invalid move")
            continue
def place_move(user_move, current_player):
    global board
    for row in reversed(range(6)):
        if board[(row * 7 + user_move) - 1] == "_":
            board[(row * 7 + user_move) - 1] = f"{player_repr[current_player]}{text_colors[3]}O{text_colors[4]}"
            break
def win_check():
    def validate(mark, orientation):
        spacing = 0
        if orientation == "horizontal":
            spacing = 1
        elif orientation == "vertical":
            spacing = 7
        elif orientation == "diagonal 6":
            spacing = 6
        elif orientation == "diagonal 8":
            spacing = 8
        count = 1
        mark = sorted(mark)
        for i in range(1, len(mark)):
            if mark[i] == mark[i-1] + spacing:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 1
        return False
    def check(orientation, orientation_text):
        red_mark = []
        yellow_mark = []
        for square in orientation:
            for index in square:
                if board[index] != "_":
                    if '\033[31m' in board[index]:
                        red_mark.append(index)
                    elif '\033[33m' in board[index]:
                        yellow_mark.append(index)
            if len(sorted(red_mark)) >= 4:   
                if validate(red_mark, orientation_text):
                    return True
            elif len(sorted(yellow_mark)) >= 4:   
                if validate(yellow_mark, orientation_text):
                    return True
            red_mark = []
            yellow_mark = []
        return False

    #check horizontal wins
    if check(rows, "horizontal"):
        return True
    #check vertical wins
    if check(columns, "vertical"):
        return True
    #check diagonal wins
    if check(diagonals_6, "diagonal 6"):
        return True
    if check(diagonals_8, "diagonal 8"):
        return True

current_player = 0
ongoing = False
while True:
    if not ongoing:
        col, current_player = decide_first_player()
        print_board()
        ongoing = True
    user_move = user_makes_move(col, current_player)
    place_move(user_move, current_player)
    print_board()

    if win_check():
        print(f"{current_player}{text_colors[4]} wins!\n")
        board = ["_"] * 42
        ongoing = False
    else:
        if current_player == text_colors[2] + "Yellow":
            current_player = text_colors[1] + "Red"
        elif current_player == text_colors[1] + "Red":
            current_player = text_colors[2] + "Yellow"