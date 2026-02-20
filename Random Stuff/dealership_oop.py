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

    def __repr__(self):
        return f"${self.price}.00 USD: {self.brand} {self.model} {self.year}, {self.color}, {self.miles} miles, {self.fuel_range} mile range"

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

    def __repr__(self):
        base = super().__repr__()
        return f"{base}, {self.payload_capacity} lbs payload capacity, {self.bed_length} ft bed, {self.towing_capacity} lbs towing capacity"

class Car(Vehicle):
    def __init__(self, brand, model, year, color, price, miles, fuel_range, seating_capacity, cargo_volume, doors):
        super().__init__(brand, model, year, color, price, miles, fuel_range)
        self.seating_capacity = seating_capacity
        self.cargo_volume = cargo_volume
        self.doors = doors

    def __repr__(self):
        base = super().__repr__()
        return f"{base}, {self.seating_capacity} seats, {self.cargo_volume} cubic ft cargo capacity, {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, price, miles, fuel_range, engine_displacement, seat_height, wheelbase):
        super().__init__(brand, model, year, color, price, miles, fuel_range)
        self.engine_displacement = engine_displacement
        self.seat_height = seat_height
        self.wheelbase = wheelbase

    def __repr__(self):
        base = super().__repr__()
        return f"{base}, {self.engine_displacement} cc engine, {self.seat_height} in seat height, {self.wheelbase} in wheelbase"

def display(vehicle_type):
    for vehicle in display_select[vehicle_type]:
        print(vehicle)

trucks = [
    Truck("Ford", "F-150 Raptor", 2026, "Red", 95000, 120, 400, 3500, 6.5, 14000),
    Truck("Chevrolet", "Silverado 3500HD", 2025, "Black", 88000, 50, 450, 4200, 8.0, 16000),
    Truck("Ram", "2500 Power Wagon", 2024, "White", 105000, 200, 500, 3900, 6.5, 15000),
]
cars = [
    Car("Tesla", "Model S Plaid", 2026, "Pearl White", 125000, 10, 370, 5, 28, 4),
    Car("BMW", "7 Series", 2025, "Midnight Blue", 98000, 5, 400, 5, 20, 4),
    Car("Mercedes-Benz", "S-Class Maybach", 2026, "Obsidian Black", 210000, 2, 430, 5, 22, 4),
]
motorcycles = [
    Motorcycle("Harley-Davidson", "CVO Limited", 2026, "Gloss Black", 55000, 0, 250, 1923, 27, 66),
    Motorcycle("Ducati", "Panigale V4", 2025, "Red", 36000, 100, 180, 1103, 32, 56),
    Motorcycle("BMW", "R 18 Transcontinental", 2026, "Blue", 43000, 50, 300, 1802, 29, 67),
]
display_select = {
    'c': cars,
    't': trucks,
    'm': motorcycles
}

print("(You have 381,000 dollars in the bank upon visiting the dealership)")
print("Welcome to our dealership, where we sell totally-fairly-priced vehicles and specialize in unfairly collecting large sums of money!")

while True:
    selection = input("Would you like to check out our available cars ('c'), trucks ('t'), or motorcycles ('m')?\n>").lower()
    if selection not in ['c', 't', 'm']:
        print("\nInvalid option.\n")
        continue
    else:
        display(selection)
        print()
        print("See anything you like?\n('1' for first, '2' for second, '3' for third)")