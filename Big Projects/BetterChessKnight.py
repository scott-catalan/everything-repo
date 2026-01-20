column = {"a": 1, "b": 2, "c": 3, "d": 4, 
          "e": 5, "f": 6, "g": 7, "h": 8}
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

def EXECUTE(new, current):
    newpos = (column[new[0]], int(new[1]))
    currentpos = (column[current[0]], int(current[1]))

    finalmove = (currentpos[0] - newpos[0], 
                currentpos[1] - newpos[1])

    if finalmove in moves:
        return True
    else:
        return False

current = "d4"
while True:
    new = input(f"The knight is currently on {current}. Where would you like to move it?\n>")
    if len(new) == 2 and new[0] in "abcdefgh" and new[1] in "12345678":
        if EXECUTE(new, current):
            current = new
            print(f"Moved to {current}")
        else: 
            print("Invalid knight move")
    else:
        print("Invalid chess notation")