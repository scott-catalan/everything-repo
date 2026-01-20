import random
print("Pick rock, paper, or scissors")
user = input()
enemy = random.randint(1,3)
if enemy == 1:
    enemy = "rock"
elif enemy == 2:
    enemy = "paper"
elif enemy == 3:
    enemy = "scissors"
if user == "rock" or user == "paper" or user == "scissors":
    if user == enemy:
        print("Enemy picked the same option. It is a tie")
    elif user == "rock" and enemy == "scissors":
        print("Enemy picked scissors. You win")
    elif user == "scissors" and enemy == "paper":
        print("Enemy picked paper. You win")
    elif user == "paper" and enemy == "rock":
        print("Enemy picked rock. You win")
    elif user == "rock" and enemy == "paper":
        print("Enemy picked paper. You lose")
    elif user == "scissors" and enemy == "rock":
        print("Enemy picked rock. You lose")
    elif user == "paper" and enemy == "scissors":
        print("Enemy picked scissors. You lose")
else:
    print("Must be rock, paper, or scissors")


