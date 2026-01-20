import tkinter as tk

root = tk.Tk()
root.title("iaMalISTbUTaLSOnOTalISTbUTaLSOalISTbUTaLSOnOTalISTbUTaLSOalISTbUTaLSOnOTalISTbUTaLSOalIST")
root.geometry("800x1000")

listnum = 1

def sendtolist():
    global listnum
    text = enter.get()
    if text:
        list.insert(tk.END, str(listnum) + ": " + text)
        enter.delete(0, tk.END)
    listnum += 1

def deletetask():
    numdel = int(deletionchoice.get())
    list.delete(numdel - 1)

def clearall():
    list.delete(0, tk.END)

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

enter = tk.Entry(frame)
enter.grid(row = 0, column = 0)

deletionchoice = tk.Entry(frame)
deletionchoice.grid(row = 0, column = 1)

sendtask = tk.Button(frame, text = "send", command = sendtolist)
sendtask.grid(row = 1, column = 0)

delete = tk.Button(frame, text = "delete", command = deletetask)
delete.grid(row = 1, column = 1)

list = tk.Listbox(frame, width = 0, height = 0)
list.grid(row = 2, column = 0)

clear = tk.Button(frame, text = "clear all", command = clearall)
clear.grid(row = 3, column = 0)

root.mainloop()