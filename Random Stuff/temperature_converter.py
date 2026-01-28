def parse(user):
    if len(user) < 4:
        print("Missing essential input")
        return False
    if user[-3].upper() in "CFK":
        unit = user[-3].upper()
    else:
        print("Must contain C/F/K in the third-final character")
        return False

    if user[-2].lower() == "t":
        pass
    else:
        print("Must contain t (to) in the second-final character")
        return False

    if user[-1].upper() in "CFK" and user[-1] != unit:
        convert = user[-1].upper()
    else:
        print("Must contain C/F/K in final character, and must be distinct from the third-final character")
        return False

    num = ""
    decimal_check = 0
    negative_check = 0

    for i in range(len(user) - 3):
            num += user[i]
    
    for i in range(len(num)):
        if num[i] in "0123456789":
            pass
        elif num[i] == ".":
            decimal_check += 1
        elif num[i] == "-":
            if i == 0:
                negative_check = 1
            else:
                print("Negative sign must be placed before the first digit")
                return False
        else:
            print("Cannot contain non-numbers")
            return False
        
        if num[i] == ".":
            if i > negative_check and i < len(user) - 4:
                pass
            else:
                print("Decimals cannot be the first or final digit of the number")
                return False
            if decimal_check > 1:
                print("There can be no more than one decimal")
                return False
            else:
                pass
        else:
            pass
    
    num = float(num)
    return num, unit, convert

while True:
    user = input("\nTemperature (e.g. 50FtC, 2887CtF, 12CtK):\n>")
    result = parse(user)
    if not result:
        continue
    num, unit, convert = result

    if unit == "C" and convert == "F":
        newnum = (num * 9/5) + 32
    elif unit == "C" and convert == "K":
        newnum = num + 273.15
    elif unit == "F" and convert == "C":
        newnum = (num - 32) * 5/9
    elif unit == "F" and convert == "K":
        newnum = (num - 32) * 5/9 + 273.15
    elif unit == "K" and convert == "C":
        newnum = num - 273.15
    elif unit == "K" and convert == "F":
        newnum = (num - 273.15) * 9/5 + 32

    print(f"{num}{unit} converted to {convert} is {round(newnum, 4)}{convert}")