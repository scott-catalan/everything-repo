#Made in 2/3

from datetime import datetime
import time, random

items_stocked = [
    "apples", "milk", "bread", "chicken", "eggs"
]
items_receipted = {
    "apples": "FRESH FARMS GALA APPLES 2LB",
    "milk": "CHARLIE'S LOWFAT MILK 1GAL",
    "bread": "BREADWAY WHOLE WHEAT 24OZ",
    "chicken": "FRESH FARM CHICKEN BREAST 1LB",
    "eggs": "GRADE A LARGE EGGS 12C"
    }
items_prices = {
    "apples": 3.39, 
    "milk": 4.39,
    "bread": 2.98, 
    "chicken": 5.98, 
    "eggs": 2.98
}

liked_foods = []
hated_foods = []
liked_responses = [
    "{}? Classic move, can’t go wrong with that!",
    "Ah, {}! Absolutely top-tier taste.",
    "Nice, {}. That’s a chef-approved pick.",
    "Honestly, {} is peak grocery shopping.",
    "You picked {}? Bold and brilliant."
]
hated_responses = [
    "{}? Really? I literally don’t get it.",
    "Ugh, {}… I have strong feelings about avoiding that.",
    "Wow, {}. Someone’s brave, I’ll give you that.",
    "Huh, {}. Not my fave, but okay.",
    "Seriously with {}? That’s… ambitious."
]

transaction = 0

hyphen_break = "-" * 50

def create_receipt(time, date, transaction_num):
    receipt = f"""
    MEGA MART SUPERCENTRE
    1847 W ALDERSTONE AVE
    Brookhaven, ST 48392 USA
    TEL: (555) 014-9283
    www.megamartsupercentre.com
    Store #71   {date}   {time}
    {hyphen_break}
    {transaction_num}
    """

    print(receipt)

def get_datetime():
    time = datetime.now()
    date = datetime.now()
    return time.strftime("%I:%M %p"), date.strftime("%m/%d/%Y")

def get_transaction_num(transaction):
    fodder = "0" * (12 - len(str(transaction)))
    transaction += 1
    return fodder, transaction

for i in range(len(items_stocked)):
    if i % 3 in (1, 2):
        liked_foods.append(items_stocked[i])
    else:
        hated_foods.append(items_stocked[i])

print("Welcome to MEGA M", end='', flush=True)
time.sleep(0.1)
print("A", end = '', flush=True)
time.sleep(0.6)
for i in range(41):
    print("A", end = '', flush=True)
    time.sleep(0.01)

while True:
    cart = []
    while True:
        user = input("What would you like to purchase?\n"
                     "(type 'items' to see items)\n"
                     "(type 'done' to finalize cart)\n>").lower()
        
        if user == "items":
            print("\nOh, wanna see our stock?")
            time.sleep(1)
            print("Let me check.")
            for i in range(3): 
                time.sleep(0.7)
                print("." * (i + 1))
            time.sleep(0.7)

            shuffled_items = items_stocked[:] 
            random.shuffle(shuffled_items)
    
            print("Okay, we have")
            for i in range(len(items_stocked)):
                if i == len(shuffled_items) - 1:
                    time.sleep(0.7)
                    print(f"and {shuffled_items[i]}.")
                else:
                    time.sleep(0.7)
                    print(f"{shuffled_items[i]}, ")
            time.sleep(2)
        elif user in items_stocked:
            cart.append(user)
            if user in liked_foods:
                print(random.choice(liked_responses).format(user))
                print("")
            elif user in hated_foods:
                print(random.choice(hated_responses).format(user))
                print("")
        elif user == "done":
            pass
        else:
            time.sleep(2)
            print("Not in stock, sorry. Find another store for that.")

        cart = ["apples", "apples", "milk", "apples", "bread"]

    time, date = get_datetime()

    fodder, transaction = get_transaction_num(transaction)
    transaction_num = fodder + str(transaction)

    complete_receipt = create_receipt(time, date, transaction_num)