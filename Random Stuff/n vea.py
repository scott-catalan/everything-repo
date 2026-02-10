#Made in 1/10

import tkinter as tk

btnrow = 1

root = tk.Tk()
root.title("IAMUNRAVELING")
root.geometry("400x400")

def APPLE():
    global btnrow
    button = tk.Button(frame, text = "Button " + str(btnrow))
    button.grid(row = btnrow, column = 0)
    btnrow += 1

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

thisisabutton = tk.Button(frame, text = "Button Generator", command = APPLE)
thisisabutton.grid(row = 0, column = 0)

root.mainloop()