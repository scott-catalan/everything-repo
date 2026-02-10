#Made in 1/15

board = [
    [1, 2, 3, 4, 5, 6, 7, 8],        # row 1 (bottom)
    [9, 10, 11, 12, 13, 14, 15, 16], 
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64] # row 8 (top)
]
let2num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
num2let = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
col = 0
row = 0

def CONVERT(move):
    col = let2num[move[0]]
    row = int(move[1]) - 1
    pos = board[row][col]
    return pos

def REVERT(pos):
    for r in range(8):
        for c in range(8):
            if board[r][c] == pos:
                col = num2let[c]
                row = str(r + 1)
                move = col + row
                return move

def VALIDATE(user, current):
    diff = (current - user)
    if diff in (-17, -15, -10, -6, 6, 10, 15, 17):
        return True
    else:
        return False

now = "d4"
while True:
    kNot = input(f"The knight is currently on {now}. Where would you like to move it?\n>")
    if len(kNot) == 2 and kNot[0] in "abcdefgh" and kNot[1] in "12345678":
        user = CONVERT(kNot)
        current = CONVERT(now)
        if VALIDATE(user, current):
            print(f"Valid move! Now on {kNot}.")
            now = kNot
        else:
            print("Invalid knight move.")
    else:
        print("Invalid chess notation.")