import random
import time
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_']
correct = 0
total = 0
for z in range(1, 50):
    print("")
while True:
    match = 0
    password = ''
    try:
        length = int(input("Password character length:\n>"))
        try:
            sec = int(input("How much time (in seconds):\n>"))
        except ValueError:
            print("Must be an positive whole number.")
            continue
        if length < 1:
            print("Must be greater than 0.")
            continue
        for i in range(0, length):
            password += random.choice(characters)
        print(password)
        for num in range(sec, 0, -1):
            time.sleep(1)
        for p in range(1, 50):
            print("")
        print("Time is up!")
        ans = input("What was the password?\n>")
        total += 1
        if ans == password:
            print("\nYou correctly memorized the password.\n")
            correct += 1
        else:
            print("\nYou failed to memorize the password.\n")
            print(f"Current score: {correct}/{total}")
            for s in range(0, len(password)):
                passchar = password[s]
                try: 
                    anschar = ans[s]
                    if passchar == anschar:
                        match += 1
                except IndexError:
                    break
            print(f"Accuracy: {(match / len(password)) * 100}%\n")  
    except ValueError:
        print("Must be an integer.")