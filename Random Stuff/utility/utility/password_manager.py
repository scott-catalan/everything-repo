import tkinter as tk

root = tk.Tk()
root.title("totallynotavirus.com")
root.geometry("400x400")

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

s1 = "d9Sq1"
s2 = "t3$-s"
s3 = "_01]A"
s4 = "lOSp:"
s5 = "*.e9S"
s6 = "$ps.."
s7 = "ll0.2"
s8 = "=_see"
s9 = "m8Ws0"
s10 = "$$mgE"
s11 = "lSAs1"
s12 = "os)6^"
s13 = "72]pA"
s14 = "}2e3d"
s15 = "!?sg%"

cycle1 = 1
cycle2 = 6
cycle3 = 2



def EXECUTE():
    if web.get() != '':
        if user.get() != '':
            if password.get() != '':
                    weblist.insert(tk.END, web.get())
                    web.delete(0, tk.END)
                    userlist.insert(tk.END, user.get())
                    user.delete(0, tk.END)
                    passwordlist.insert(tk.END, password.get())
                    password.delete(0, tk.END)

def deletetask():
    numdel = int(deletionchoice.get())
    weblist.delete(numdel - 1)
    userlist.delete(numdel - 1)
    passwordlist.delete(numdel - 1)
    deletionchoice.delete(0, tk.END)

def GENERATE():
    global cycle1, cycle2, cycle3, cycle4, cycle5
    if cycle1 >= 14:
        cycle1 -= 13
    cycle1 += 1
    if cycle2 <= 1:
        cycle2 += 13
    cycle2 -= 1
    if cycle3 >= 14:
        cycle3 -= 11
    cycle3 += 2
    gp = "" #generated password
    if cycle1 == 1:
        gp += s1
    elif cycle1 == 2:
        gp += s2
    elif cycle1 == 3:
        gp += s3
    elif cycle1 == 4:
        gp += s4
    elif cycle1 == 5:
        gp += s5
    elif cycle1 == 6:
        gp += s6
    elif cycle1 == 7:
        gp += s7
    elif cycle1 == 8:
        gp += s8
    elif cycle1 == 9:
        gp += s9
    elif cycle1 == 10:
        gp += s10
    elif cycle1 == 11:
        gp += s11
    elif cycle1 == 12:
        gp += s12
    elif cycle1 == 13:
        gp += s13
    elif cycle1 == 14:
        gp += s14
    elif cycle1 == 15:
        gp += s15
    if cycle2 == 1:
        gp += s1
    elif cycle2 == 2:
        gp += s2
    elif cycle2 == 3:
        gp += s3
    elif cycle2 == 4:
        gp += s4
    elif cycle2 == 5:
        gp += s5
    elif cycle2 == 6:
        gp += s6
    elif cycle2 == 7:
        gp += s7
    elif cycle2 == 8:
        gp += s8
    elif cycle2 == 9:
        gp += s9
    elif cycle2 == 10:
        gp += s10
    elif cycle2 == 11:
        gp += s11
    elif cycle2 == 12:
        gp += s12
    elif cycle2 == 13:
        gp += s13
    elif cycle2 == 14:
        gp += s14
    elif cycle2 == 15:
        gp += s15
    if cycle3 == 1:
        gp += s1
    elif cycle3 == 2:
        gp += s2
    elif cycle3 == 3:
        gp += s3
    elif cycle3 == 4:
        gp += s4
    elif cycle3 == 5:
        gp += s5
    elif cycle3 == 6:
        gp += s6
    elif cycle3 == 7:
        gp += s7
    elif cycle3 == 8:
        gp += s8
    elif cycle3 == 9:
        gp += s9
    elif cycle3 == 10:
        gp += s10
    elif cycle3 == 11:
        gp += s11
    elif cycle3 == 12:
        gp += s12
    elif cycle3 == 13:
        gp += s13
    elif cycle3 == 14:
        gp += s14
    elif cycle3 == 15:
        gp += s15
    password.delete(0, tk.END)
    password.insert(tk.END, gp)
    

web = tk.Entry(frame)
web.grid(row = 0, column = 0)
user = tk.Entry(frame)
user.grid(row = 0, column = 1)
password = tk.Entry(frame)
password.grid(row = 0, column = 2)

save = tk.Button(frame, text = "Save", command=EXECUTE)
save.grid(row = 1, column = 1)

weblist = tk.Listbox(frame, height = 0)
weblist.grid(row = 2, column = 0)
userlist = tk.Listbox(frame, height = 0)
userlist.grid(row = 2, column = 1)
passwordlist = tk.Listbox(frame, height = 0)
passwordlist.grid(row = 2, column = 2)

deletionchoice = tk.Entry(frame)
deletionchoice.grid(row = 4, column = 1)

delete = tk.Button(frame, text = "Delete", command = deletetask)
delete.grid(row = 5, column = 1)

generate = tk.Button(frame, text = "Generate Password", command=GENERATE)
generate.grid(row = 1, column = 2)

root.mainloop()