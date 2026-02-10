#Made in 1/19

import os, sys
from tkinter import *
from wordleLogic import WORD, WORDS, GUESSES, CALCULATE

# This finds the "true" root folder whether running as a script or an EXE
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Now use BASE_DIR for everything
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
WORDS_PATH = os.path.join(ASSETS_DIR, 'words.txt')
GUESSES_PATH = os.path.join(ASSETS_DIR, 'guesses.txt')
ICON_PATH = os.path.join(ASSETS_DIR, 'logo.png')

colors = {0: '#787C7F', 1: "#D2C564", 2: '#6AAA64'}
currentRow = 0
words = WORDS()
guesses = GUESSES()
word = WORD(words)

def GUESS():
    global currentRow
    user = userInput.get()
    if user in guesses:
        guess = CALCULATE(user, word)
        for i in range(5):
            grid[currentRow][i].config(text = user[i], bg = colors[guess[i]])
        currentRow += 1
        
        if guess == [2, 2, 2, 2, 2]:
            winLoss.config(text="WIN")
            userInput.config(state="disabled")
        elif currentRow == 6:
            winLoss.config(text=f"LOSE - Word was {word}")
            userInput.config(state="disabled")

        userInput.delete(0, END)
    else:
        print("Not in list")

window = Tk()
window.geometry("500x500")
window.title("Wordle")
window.config(background = "#131313")
icon = PhotoImage(file = ICON_PATH)
window.iconphoto(True, icon)

frame1 = Frame(window)
frame1.grid(row = 0, column = 0)

frame2 = Frame(window)
frame2.grid(row = 1, column = 0)

frame3 = Frame(window)
frame3.grid(row = 2, column = 0)

winLoss = Label(frame1, text = "", fg = "#ffffff", bg = "#131313")
winLoss.pack()

grid = []
for row in range(6):
    rowLabels = []
    for col in range(5):
        label = Label(frame2, text = "_")
        label.grid(row = row, column = col)
        rowLabels.append(label)
    grid.append(rowLabels)
    
userInput = Entry(frame3)
userInput.bind('<Return>', lambda event: GUESS())
userInput.pack()

window.mainloop()