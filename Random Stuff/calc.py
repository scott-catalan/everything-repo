import tkinter as tk

root = tk.Tk()
root.title("KindaCalculatorButAlsoNotReally?")
root.geometry("400x200")

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

symbol = "+"
cycle = 2

def CHANGE():
    global in1, in2, out1, plus, equals, result, symbol, cycle
    if cycle == 1:
        symbol = "+"
        cycle = 2
    elif cycle == 2:
        symbol = "-"
        cycle = 3
    elif cycle == 3:
        symbol = "x"
        cycle = 4
    elif cycle == 4:
        symbol = "/"
        cycle = 1
    plus.config(text = symbol)

def EXECUTE():
    global in1, in2, out1, plus, equals, result, symbol, cycle
    num1 = int(in1.get())
    num2 = int(in2.get())
    if cycle == 2:
        out1.insert(0, str(num1 + num2))
    if cycle == 3:
        out1.insert(0, str(num1 - num2))
    if cycle == 4:
        out1.insert(0, str(num1 * num2))
    if cycle == 1:
        out1.insert(0, str(num1 / num2))

in1 = tk.Entry(frame)
in1.grid(row = 0, column = 0)
in2 = tk.Entry(frame)
in2.grid(row = 0, column = 2)
out1 = tk.Entry(frame)
out1.grid(row = 0, column = 4)

plus = tk.Button(frame, text = str(symbol), command = CHANGE)
plus.grid(row = 0, column = 1)
equals = tk.Button(frame, text = "=", command = EXECUTE)
equals.grid(row = 0, column = 3)

root.mainloop()