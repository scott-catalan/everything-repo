import random
import time
valid = {"r": "rock", "p": "paper", "s": "scissors"}
wintext = (
    "How?!?", 
    "Are you cheating?", 
    "Did you seriously just... wow...", 
    "You must be psychic.", 
    "Lucky guess, Ill give you that.", 
    "Wow... a win. Celebrate while it lasts.",
    "Agh! Fuck you.")
losetext = (
    "Wow, imagine getting beaten by a bot.", 
    "Haha! Gotcha!", 
    "Sucks to suck :P", 
    "Are you even trying?",
    "You call that a move?", 
    "Even my grandma could beat that.", 
    "Seriously? Thats all you got?", 
    "Ive seen toddlers play better.")
tietext = (
    "Stalemate. Booooring...", 
    "Another tie. How thrilling.", 
    "Tie? That's sad.", 
    "We are just wasting time now.", 
    "Groundhog Day all over again.", 
    "Yawn... tie again.", 
    "Let us call this a mutually disappointing draw.")
w = 0
l = 0
t = 0
r = 0
print("You are playing Rock-Paper-Scissors against me.")
while True:
    r += 1
    bot = random.choice(list(valid.keys()))
    move = input(f"\nRound {r}!\nEnter your move: (r)ock (p)aper (s)cissors:\n>")
    if move in valid:
        print(f"\nYou chose {valid[move]}.")
        time.sleep(2)
        print("Alright, my turn...") 
        for i in range(3):
            time.sleep(0.8)
            print(".")
        time.sleep(0.8)
        print(f"I choose {valid[bot]}.\n")
        time.sleep(1.5)
        if move == bot:
            print(random.choice(tietext))
            t += 1
        elif (move == "r" and bot == "s") or \
            (move == "s" and bot == "p") or \
            (move == "p" and bot == "r"):
            print(random.choice(wintext))
            w += 1
        else:
            print(random.choice(losetext))
            l += 1
        print(f"\nCurrent Win-Loss-Tie: {str(w)}/{str(l)}/{str(t)}")
    else:
        print("\nInvalid input. Must be r, p, or s.\n")


