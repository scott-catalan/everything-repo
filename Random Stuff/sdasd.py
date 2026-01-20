import tkinter as tk

def insert_text():
    entry.insert(0, "Hello World")

root = tk.Tk()
entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Insert Text", command=insert_text)
button.pack()

root.mainloop()