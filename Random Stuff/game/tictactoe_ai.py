'''
# Project Creation Date: 3:03:53 PM, 2/25/2026
'''
import time

board = [str(i) for i in range(9)]
win_states = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    [0, 4, 8],
    [2, 4, 6],
]
turns = {
    0: "X",
    1: "O"
}
outcome = {
    0: "X wins!",
    1: "O wins!",
    2: "Its a tie!"
}

def print_board():
    print("")
    for i in range(9):
        print(f"{board[i]}", end='')
        if i % 3 != 2:
            print(" | ", end='')
        else:
            if i != 8:
                print("\n==========")  
    print("\n")
def gamestate_check():
    for line in win_states:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            if board[line[0]] == "X":
                return 0
            if board[line[0]] == "O":
                return 1
    for i in board:
        if i not in ["X", "O"]:
            return 3
    return 2
def make_move(turn, square):
    if board[int(square)].isdecimal():
        board[int(square)] = turns[turn]
        print_board()
        return True, gamestate_check()
    else:
        return False, None

def calculate_AI(board, depth, current_turn):
    state = gamestate_check()
    if state != 3:
        if state == 0:
            return -10 + depth
        elif state == 1:
            return 10 - depth
        else:
            return 0
            
    if current_turn == 1:
        best_score = -50000
        for i in range(9):
            if board[i].isdecimal():
                board[i] = "O"
                score = calculate_AI(board, depth + 1, False)
                board[i] = str(i)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 50000
        for i in range(9):
            if board[i].isdecimal():
                board[i] = "X"
                score = calculate_AI(board, depth + 1, True)
                board[i] = str(i)
                best_score = min(best_score, score)
        return best_score
def AI_move():
    best_move = None
    best_score = -50000
    for i in range(9):
        if board[i].isdecimal():
            board[i] = "O"
            score = calculate_AI(board, 0, 1)
            board[i] = str(i)
            if score > best_score:
                best_score = score
                best_move = i
    return make_move(1, best_move)

print("Here's the starting board:")
time.sleep(0.5)
print_board()
time.sleep(1)
print("You are X, the AI is O\n")
time.sleep(1)

while True:
    user = input("Make your move:\n>")
    if user not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Syntax Error")
        continue
    
    occupied_check, gamestate = make_move(0, user)
    
    if not occupied_check:
        print("Occupied Square")
        continue
    
    if gamestate != 3:
        print(outcome[gamestate])
        break
    
    time.sleep(0.5)
    print("AI's turn")
    time.sleep(1)
    
    _, gamestate = AI_move()

    if gamestate != 3:
        print(outcome[gamestate])
        break