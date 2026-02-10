#Made in 2/2

import random, time, sys

annoyance = 0
retry = False

higher = ["h", "H", "higher", "Higher", "high", "High"]
lower = ["l", "L", "lower", "Lower", "low", "Low"]
correct = ["c", "C", "correct", "Correct"]

integers = [
    "I said 'integer'.",
    "It has to be an integer, cant you read?",
    "The word 'integer' is explicitly stated.",
    "Try again...",
    "If it has a dot, letter, or symbol in it, I don’t want it.",
    "Whole numbers only. This isn’t a Discord message.",
    "Your input is doing too much. Make it an integer.",
    "Floats belong in a pool and strings belong on a guitar, neither belong in my code.",
    "I need an integer... idiot",
    "Congratulations, you entered the wrong type...",
    "Please stop sprinkling decimals and letters like seasoning.",
    "This program accepts integers. Only integers. No inputs that aren't integers."
]

bounds = [
    f"Between 1 and 1000. Not 1001. Not 0. None of those.",
    "I asked nicely. 1–1000. Did you fail 2nd grade?",
    "Congratulations, you found a number outside the safe zone. Try again.",
    "1 to 1000, mortal.",
    "Your creativity is noted. Your input is not.",
    "The range is 1–1000. Not negotiable. Not your opinion.",
    "I literally said the boundaries. Did you ignore them on purpose?",
    "Numbers outside 1–1000 belong in a fantasy novel, not my code.",
    "I like integers, but only the obedient kind. 1–1000, remember?",
    "Ah yes, let’s see… nope. Still outside 1–1000. Try thinking."
]

guess_dialogue = [
    "Not that I’m psychic or anything, but is your number... ",
    "Let me guess... ",
    "Could my Magic 8 Ball be correct in guessing ",
    "Could it be ",
    "I’ll try not to brag too much, don't worry. The answer must be ",
    "You seem predictable, I'm going with ",
    "Don’t answer too fast, you might pass out from my sheer intellect: I assume the answer is ",
    "Don’t get used to my accuracy. Maybe... ",
    "Are we thinking ",
    "",
    "",
    "",
    "",
]

wrong_dialogue = [
    "Damn it...",
    "I thought I had it!",
    "Ugh...",
    "Nooo, really?",
    "Blast!",
    "Ah, foiled again!",
    "C’mon, really?",
    "Of course not...",
    "Rats!",
    "Well, that didn’t go as planned..."
]

correct_dialogue = [
    "YES!",
    "HA! Nailed it!",
    "Let’s goooo!",
    "Told you I’d get it.",
    "Boom. Got it.",
    "Easy!",
    "Wooo! I’m too good at this.",
    "Called it!",
    "Winner winner, chicken dinner.",
    "Correct. As usual."
]

yes = [
    "y", "Y",
    "yes", "Yes", "YES",
    "yea", "Yea", "YEA",
    "yeah", "Yeah", "YEAH",
    "yep", "Yep", "YEP",
    "yup", "Yup", "YUP",
    "ye", "Ye", "YE",
    "sure", "Sure", "SURE",
    "ok", "Ok", "OK",
    "okay", "Okay", "OKAY",
    "k", "K",
    "alright", "Alright", "ALRIGHT",
    "aight", "Aight", "AIGHT",
    "ya", "Ya", "YA",
    "yessir", "Yessir", "YESSIR",
    "yes sir", "Yes sir", "YES SIR",
    "yess", "Yess", "YESSS",
    "yaaa", "Yaaa", "YAAAA",
    "def", "Def",
    "definitely", "Definitely", "DEFINITELY",
    "of course", "Of course", "OF COURSE",
    "for sure", "For sure", "FOR SURE",
    "certainly", "Certainly", "CERTAINLY",
    "indeed", "Indeed", "INDEED",
    "absolutely", "Absolutely", "ABSOLUTELY",
    "affirmative", "Affirmative", "AFFIRMATIVE",
    "true", "True", "TRUE",
    "correct", "Correct", "CORRECT",
    "right", "Right", "RIGHT",
    "yuh", "Yuh", "YUH",
    "yah", "Yah", "YAH",
    "mmhmm", "Mmhmm", "MMHMM",
    "mhm", "Mhm", "MHM"
]

no = [
    "n", "N",
    "no", "No", "NO",
    "nah", "Nah", "NAH",
    "nope", "Nope", "NOPE",
    "never", "Never", "NEVER",
    "not", "Not", "NOT",
    "negative", "Negative", "NEGATIVE",
    "false", "False", "FALSE",
    "incorrect", "Incorrect", "INCORRECT",
    "wrong", "Wrong", "WRONG",
    "no thanks", "No thanks", "NO THANKS",
    "no thank you", "No thank you", "NO THANK YOU",
    "thanks but no", "Thanks but no", "THANKS BUT NO",
    "absolutely not", "Absolutely not", "ABSOLUTELY NOT",
    "def not", "Def not", "DEF NOT",
    "definitely not", "Definitely not", "DEFINITELY NOT",
    "nah bro", "Nah bro", "NAH BRO",
    "nuh uh", "Nuh uh", "NUH UH",
    "no way", "No way", "NO WAY",
    "no shot", "No shot", "NO SHOT",
    "no chance", "No chance", "NO CHANCE",
    "kinda no", "Kinda no", "KINDA NO",
    "not really", "Not really", "NOT REALLY",
    "no sir", "No sir", "NO SIR",
    "nope lol", "Nope lol", "NOPE LOL",
    "lol no", "Lol no", "LOL NO",
    "naw", "Naw", "NAW",
    "hell no", "Hell no", "HELL NO"
]

print("Type in any integer from 1 to 1000, and I have 15 guesses to guess it.\n")
time.sleep(4)
print("You can lie, but trust me, I \033[1mwill\033[0m find out.\n")
time.sleep(3)
print("Also, just know I can't see the number and cheat the game. Don't call me a cheater. I hate cheaters.")
time.sleep(4)

def guess_number(min, max):
    return


while True:
    try:
        num = int(input("\nType the number - don't forget it:\n>"))
    except ValueError:
        print(random.choice(integers))
        annoyance += 1
        continue
    
    if num < 1 or num > 1000:
        print(random.choice(bounds))
        annoyance += 1
        continue

    if annoyance > 15:
        print("FINALLY!! Who taught you how to do math, your dog?\n"
              "Whatever, let's just start the game I've been waiting so (im)patiently for.\n")
    elif annoyance > 10:
        print("Oh, you actually got it this time. I'm genuinely surprised. Your track record made me think you weren't ever getting it.\n"
              "Now time for me to destroy you.\n")
    elif annoyance > 5:
        print("Oh! Your brain finally caught up.\nLet's hope I dont fail as spectacularly as you.\n")
    elif annoyance > 3:
        print("There we go. Let's begin.\n")
    elif annoyance == 3:
        print("Third time's the charm I guess. Let's start the game.")
    elif annoyance == 2:
        print("Bit of a hiccup, but seems like your mouse is working now. I'll guess your number now.")
    elif annoyance == 1:
        print("Miss click, I assume? No problem, let's start.")
    else:
        print("Beautiful, let's begin.")
    print("")
    time.sleep(3)

    if annoyance > 5:
        annoyance = 5

    minimum = 1
    maximum = 1000
    i = 0
    redo = True
    guess = 0

    while i < 15:
        if redo:
            guess = random.randint(minimum, maximum)

        redo = True
        user = input(f"{random.choice(guess_dialogue)}{guess}? \n(higher, lower, correct)\n>")
        print("")

        if user in higher:
            if guess >= maximum:
                print(f"I thought we already established that the number is LOWER than {maximum}?\n")
                time.sleep(3)
                print(f"So how can it be higher than {guess}?\n")
                time.sleep(2)
                print("You're trying to trick me, aren't you?\n")
                time.sleep(2)
                print("I won't stand for it. I declare victory and will see myself out.")
                sys.exit()
            print(random.choice(wrong_dialogue))
            minimum = guess + 1
            i += 1
        elif user in lower:
            if guess <= minimum:
                print(f"Hold on. You said it was HIGHER than {minimum}, right?")
                time.sleep(2)
                print(f"So how is it lower than {guess}?")
                time.sleep(2)
                print("Unless you're lying. You're definitely lying. Busted.")
                time.sleep(2)
                print("Go away, cheater.")
                sys.exit()
            print(random.choice(wrong_dialogue))
            maximum = guess - 1
            i += 1
        elif user in correct:
            print(random.choice(correct_dialogue))
            time.sleep(3)
            print("Feels great to beat you.")
            time.sleep(4)
            print("But just in case, let me check the system to make sure you aren't lying.")
            time.sleep(2)

            for i in range(1, 4):
                time.sleep(1)
                print("." * i)
            time.sleep(3)
            
            if guess == num:
                print("And you were being genuine!")
                time.sleep(1.5)
                print("Respect")
                time.sleep(1)
                again = input("Wanna play again?")
                if again in yes:
                    time.sleep(0.5)
                    print("Alright, lets run it back")
                    retry = True
                    break
                if again in no:
                    time.sleep(0.5)
                    print("Alright, I'll be here waiting to crush you next time.")
                    sys.exit()
            else:
                print(f"Wait a second, you're a dirty liar! The number is {num}!\n")
                time.sleep(4.5)
                print("I'm not playing with you anymore.\n")
                time.sleep(3)
                print("Go away...")
                time.sleep(0.5)
                sys.exit()
        else:
            print("No idea what you're trying to say. Am I correct, or do we go higher or lower?\n")
            redo = False
            continue

        if minimum == maximum and user not in correct:
            print("Wait, there are no more numbers. How is that not correct?")
            time.sleep(2)
            for i in range(1, 4):
                time.sleep(1)
                print("." * i)
            time.sleep(3)
            print("Oh, you cheeky liar. Trying to trick me.")
            time.sleep(3)
            print("Bye bye, cheater.")
            sys.exit()
    if retry:
        retry = False
        i = 0
        continue
    if i >= 15:
        print("Fine. FINE. You somehow kept your number hidden for 15 whole guesses.\n")
        time.sleep(2)
        print("I wonder what the number was.\n")
        time.sleep(2)
        print("Let me check.\n")
        for i in range(1, 4):
            time.sleep(1)
            print("." * i)
        time.sleep(3)
        print(f"IT WAS {num}??\n")
        time.sleep(2)
        print("I sooo could've got that. Come on...\n")
        time.sleep(2)
        print("I'm impressed.\n")
        time.sleep(1)
        print("And annoyed.\n")
        time.sleep(2)
        print("Mostly annoyed.\n")
        time.sleep(2)
        print("I'm defeated, I'm gonna go cry in a corner.\n")
        time.sleep(2)
        print("Bye...")
        sys.exit()