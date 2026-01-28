import string, os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'common_passwords.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    common_passwords = set(line.strip() for line in file)

while True:
    user = input("Type your password:\n>")
    if user == "":
        print("Cannot be nothing")
        continue
    else:
        break

def password_length(user):
    length = len(user)
    if length > 20:
        return "Excellent"
    elif length > 14:
        return "Strong"
    elif length > 9:
        return "Good"
    elif length > 6:
        return "Fair"
    else:
        return "Weak"
    
def password_complexity(user):
    complexity = 0
    letters_lower = "".join(c for c in user if c in string.ascii_lowercase)
    letters_upper = "".join(c for c in user if c in string.ascii_uppercase)
    numbers = "".join(c for c in user if c in "1234567890")
    symbols = "".join(c for c in user if c in """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~""")

    if len(letters_lower) / (len(user) + 0.01) > 0.17:
        complexity += 1
    if len(letters_upper) / len(user) > 0.17:
        complexity += 1
    if len(numbers) / len(user) > 0.17:
        complexity += 1
    if len(symbols) / len(user) > 0.17:
        complexity += 1

    a = 0
    b = 0.01
    for i in range(len(user) - 1):
        if user[i] != user[i + 1]:
            a += 1
        else:
            b += 1
    if a / b > 0.2:
        complexity += 1

    if complexity > 4:
        return "Excellent"
    elif complexity > 3:
        return "Strong"
    elif complexity > 2:
        return "Good"
    elif complexity > 1:
        return "Fair"
    else:
        return "Weak"

def password_uniqueness(user):
    if user in common_passwords:
        return "Common"
    else:
        return "Unique"

def overall_strength(in1, in2, in3):
    dic = {"Weak": 1, "Fair": 2, "Good": 3, "Strong": 4, "Excellent": 5, "Common": -3, "Unique": 4}
    dic2 = {5: "Excellent", 4: "Strong", 3: "Good", 2: "Fair", 1: "Weak", 0: "Weak", -1: "Weak", -2: "Weak"}
    values = [dic[in1], dic[in2], dic[in3]]
    return dic2[round(sum(values) / 3)]

length = password_length(user)
complexity = password_complexity(user)
uniqueness = password_uniqueness(user)
strength = overall_strength(length, complexity, uniqueness)

print(f"Length: {length}")
print(f"Complexity: {complexity}")
print(f"Uniqueness: {uniqueness}")
print(f"Overall strength: {strength}")