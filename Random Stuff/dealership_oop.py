'''
# Project Creation Date: 7:23:30 PM, 2/19/2026
'''

class Vehicle:
    def __init__(self, brand, model, year, color, price, miles, fuel_range):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.miles = miles
        self.fuel_range = fuel_range

    def purchase(self, user_money):
        if user_money >= self.price:
            return f"You have successfully purchased the {self.brand} {self.model}."
        else:
            return f"Cant buy it. Too broke. Git gud."

class Truck(Vehicle):
    def __init__(self, brand, model, year, color, price, miles, fuel_range, payload_capacity, bed_length, towing_capacity):
        super().__init__(brand, model, year, color, price, miles, fuel_range)
        self.payload_capacity = payload_capacity
        self.bed_length = bed_length
        self.towing_capacity = towing_capacity

class Car(Vehicle):
    def __init__(self, brand, model, year, color, price, miles, fuel_range, seating_capacity, cargo_volume, doors):
        super().__init__(brand, model, year, color, price, miles, fuel_range)
        self.seating_capacity = seating_capacity
        self.cargo_volume = cargo_volume
        self.doors = doors

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, price, miles, fuel_range, engine_displacement, seat_height, wheelbase):
        super().__init__(brand, model, year, color, price, miles, fuel_range)
        self.engine_displacement = engine_displacement
        self.seat_height = seat_height
        self.wheelbase = wheelbase

print("Welcome to our dealership, where we sell totally-fairly-priced vehicles!")

while True:
    selection = input("Would you like to check out our available cars ('c'), trucks ('t'), or motorcycles ('m')?\n>")
    if selection not in ['c', 't', 'm']:
        print("\nInvalid option.\n")
        continue
    elif selection == 'c':
        print("")