in1 = float(input("First number: "))
in2 = float(input("Second number: "))
func = int(input("Function (1-8): "))

#add=1, subtract=2, multiply=3, divide=4
#exponent=5, tetration=6, square root=7, cube root=8

def EXECUTE(in1, in2, func):
    if func == 1:
        out = in1 + in2
    elif func == 2:
        out = in1 - in2
    elif func == 3:
        out = in1 * in2
    elif func == 4:
        if in2 == 0:
            print("Undefined")
        else:
            out = in1 / in2
    elif func == 5:
        out = in1 ** in2
    elif func == 6:
        out = in1
        for _ in range(int(in2) - 1):
            out = in1 ** out
    elif func == 7:
        out = in1 ** (1/2)
    elif func == 8:
        out = in1 ** (1/3)
    else:
        out = "Choose a function from 1 to 8"
    if not (func == 4 and in2 == 0):
        print(out)
EXECUTE(in1, in2)
