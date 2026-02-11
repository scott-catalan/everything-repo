import random
answer = random.randint(1, 20)
guess = 1
print("I am thinking of an integer from 1 to 20.")
while True:
    try:
        p = int(input("Take a guess.\n> "))
        if p > 20 or p < 1:
            print("That's not even in the range...")
            continue
        if p == answer:
            print(f"Good job! You got it in {guess} guess{"es" if guess > 1 else ""}!")
            break
        elif p < answer:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    except ValueError:
        print("That's not an integer, dumbass.")
        continue
    guess += 1
