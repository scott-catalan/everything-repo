'''
# Project Creation Date: 4:03:49 PM, 2/19/2026
'''

class Employee:
    def __init__(self, firstname, lastname, email, age, salary, position):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age
        self.salary = salary
        self.position = position
        self.fired = False

    def give_raise(self, percent):
        percent = (percent / 100) + 1
        print(f"{self.firstname} has been given a raise from {self.salary} to {int(self.salary*percent)}. Congrats!")
        self.salary *= percent
    
    def fire_employee(self):
        self.fired = True
        self.salary = 0
        self.position = "none"
        print(f"{self.firstname} has been fired.")

sarah = Employee("Sarah", "Brown", "sarahbrown8172@gmail.com", 62, 82000, "accountant")
samuel = Employee("Samuel", "Hensen", "hen.samuel@gmail.com", 24, 31000, "janitor")
megumi = Employee("Megumi", "Suzuki", "susuki.megumi.email@gmail.com", 36, 51000, "secretary")

print(f"""Oh, you wanna know our {megumi.position} salary? Well, meet {megumi.firstname}, our current secretary. 
She gets paid roughly {megumi.salary} per year.""")
print(f"""\nAnd regarding our {samuel.position}, {samuel.firstname}, we found a replacement.""")

samuel.fire_employee()

print(f"""\n{sarah.firstname}, on the other hand, has been doing wonderfully. She deserves a raise. We will give her a 10% bump!""")

sarah.give_raise(10)