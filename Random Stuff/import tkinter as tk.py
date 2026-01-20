import tkinter as tk

btnrow = 1

root = tk.Tk()
root.title("IAMUNRAVELING")

def APPLE():
    global btnrow
    button = tk.Button(frame, text = "Button " + str(btnrow))
    button.grid(row=btnrow, column=0)
    btnrow += 1

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

thisisabutton = tk.Button(frame, text = "Button Generator", command = APPLE)
thisisabutton.grid(row = 0, column = 0)

root.mainloop()