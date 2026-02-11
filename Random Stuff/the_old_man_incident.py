import time #just discovered this gem and I love it already

print("You find an old man peacefully strolling across the sidewalk.",
    "\nYou notice his backpack is open, and his full wallet is there.")

def GAME():
    print("How much money do you take?")
    punch = round(float(input(">$")), 2)
    if punch <= -1000000:
        print("Who are you? MrBeast? You just resupplied his retirement fund with", 
            "$" + str(abs(punch)) + " like a maniac. \nAlso, he bought a yacht.")
        time.sleep(2)
        print("\n...")
        time.sleep(2)
        print("\nCan I have some money too? pwetty pwease??")
    elif punch < -10000:
        print("Well someone is feeling extremely generous (and drunk) today!",
            "\nSure, he's happy and probably gonna buy something for his grandkids,",
            "\nbut how are you gonna pay your overdue rent now?")
    elif punch < -100:
        print("Pretty big gift of $" + str(abs(punch)) + " there. He thanked you and left with a smile.",
            "\nYou just now realize you used your mom's account instead of yours. Get ready when you get home...")
    elif punch < 0:
        print("What a kind soul! You gave the man $" + str(abs(punch)) + " and he strolled away happily.",
            "\nToo bad you needed that to buy your meds. Whoops...")
    elif punch == 0:
        print("You do nothing? Boooring...",
            "\nNow he walked away, and you have to live with the fact you were too cowardly to do anything.")
    elif punch > 0 and punch <= 30: 
        print("Lucky you. The man was too old to notice a measely $" + str(punch) + " missing from his wallet.",
            "\nYou walk away unnoticed. Hope you feel great about yourself.")
    elif punch > 30:
        print("Uh oh, he noticed. Turns out the man is the sensei of an elite martial arts program.",
            "\nYou're royally fucked now...")
        time.sleep(4)
        print(".")
        time.sleep(0.7)
        print("..")
        time.sleep(0.7)
        print("...")
        time.sleep(3)
        print("INCOMING!!!")
        time.sleep(0.4)
        print("You have been punched 1 time.")
        time.sleep(1.5)
        print("You have been punched 2 times.")
        time.sleep(1.5)
        print("You have been punched 3 times.")
        time.sleep(2)
        print("\n...\n")
        time.sleep(2)
        print("You have been punched " + str(int(punch) - 2) + " times.")
        time.sleep(1.5)
        print("You have been punched " + str(int(punch) - 1) + " times.")
        time.sleep(1.5)
        print("You have been punched " + str(int(punch)) + " times by the old man.\n")
        time.sleep(1.7)
        if punch > 1000:
            print("You have ceased to exist. You are now merely a concept. Forever.")
        elif punch > 300:
            print("You have been killed by the old man. All for $" + str(punch) + ". What a joke.")
        elif punch > 100:
            print("You have been severely injured. Too bad $" + str(punch) + " can't replace a femur.")
        elif punch >= 30:
            print("You have been injured. At least the $" + str(punch) + " you stole can pay for a few bandaids.")
GAME()
while True:
    r = input("\nRetry?(y/n)\n> ")
    if r == "y":
        print("Make the right decision...")
        GAME()
    elif r == "n":
        print("Coward...")
        exit()
    else:
        print("You didn't pick y or n so fuck you. Program's over. Bye.")
        exit()