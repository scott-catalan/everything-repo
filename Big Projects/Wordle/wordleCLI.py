#Made in 1/18

from wordleLogic import WORD, WORDS, GUESSES, CALCULATE
import sys

words = WORDS()
guesses = GUESSES()

while True:
    word = WORD(words)
    attempts = 1

    while attempts <= 6:
        user = input('Type a 5 letter word:\n>').lower()
        
        if user not in guesses:
            print("Not in dictionary")
            continue

        entry = CALCULATE(user, word)

        # --- WIN CHECK ---
        if user == word:
            print("You win!")
            break

        # --- DISPLAY RESULT ---
        userlist = []
        for i in range(5):
            if entry[i] == 2:
                userlist.append(user[i].upper())
            elif entry[i] == 1:
                userlist.append(user[i].lower())
            else:
                userlist.append('_')
        print(userlist)

        attempts += 1

    # --- LOSE CONDITION ---
    if user != word:
        print(f"You lose. The word was {word}")
    
    # --- RETRY ---
    a = input("Retry? (y/n)\n>").lower()
    if a == "y":
        continue
    elif a == "n":
        print("Bye")
        sys.exit()
    else:
        print("I'll assume that's a no")
        sys.exit()