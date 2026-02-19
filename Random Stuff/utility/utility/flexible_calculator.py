'''
# Project Creation Date: 8:16:33 AM, 2/13/2026
'''
import operator

def validate(user):
    user = user.replace(" ", "")
    symbols = "-+*/"
    
    #---|Reject nothing|---#
    if user == "":
        return False
    
    #---|Reject alpha|---#
    for i in user:
        if not i.isdecimal() and i not in symbols and i != ".":
            return False
    
    #---|Reject expressions with no symbols|---#
    symbol_check = ""
    for a in user:
        if a in symbols:
            symbol_check += a
    if symbol_check == "":
        return False
    
    #---|Reject irrelevant double symbols (e.g. 5++5)|---#
    for e in range(len(user)-1):
        if user[e] in symbols and user[e+1] in symbols:
            if user[e+1] != "-":
                return False

    #---|Reject multiple decimals in a single term|---#
    dec_check = False
    for o in user:
        if o == ".":
            if dec_check:
                return False
            dec_check = True
        if o in symbols:
            dec_check = False
            
    #---|Reject decimals leading into operators|---#
    for w in range(len(user)):
        if user[w] == "." and w < len(user) - 1 and not user[w+1].isdecimal():
            return False 
        
    #---|Reject expressions starting/ending with non-numbers|---#
    if not user[0].isdecimal() and user[0] != "-":
        return False
    if not user[-1].isdecimal():
        return False

    return user

def parse(user):
    terms = []
    operators = []
    temp_string = ""

    if user[0] == "-":
        user_sec = user[1:]
        temp_string += "-"
    else:
        user_sec = user

    for i in range(len(user_sec)):
        if user_sec[i].isdecimal() or user_sec[i] == ".":
            temp_string += user_sec[i]
        elif user_sec[i] == "-" and user_sec[i-1] in "-+*/":
            temp_string += user_sec[i]
        else:
            if temp_string != "":
                terms.append(temp_string)
            operators.append(user_sec[i])
            temp_string = ""
    terms.append(temp_string)

    return terms, operators

def evaluate(terms, operators):
    def make_list(terms, operators):
        evaluate_list = []
        for i in range(len(operators)):
            evaluate_list.append(float(terms[i]))
            evaluate_list.append(operators[i])
        evaluate_list.append(float(terms[-1]))
        return evaluate_list
    
    def pemd(operator, evaluate_list):
        index = evaluate_list.index(operator)
        num1, op, num2 = evaluate_list[index-1], evaluate_list[index], evaluate_list[index+1]

        del evaluate_list[index-1:index+2]
    
        try:
            result = ops[op](float(num1), float(num2))
        except ZeroDivisionError:
            return False
        evaluate_list.insert(index-1, result)
        return evaluate_list

    ops = {
        "+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": operator.truediv
        }

    evaluate_list = make_list(terms, operators)

    while "*" in evaluate_list:
        result = pemd("*", evaluate_list)
        if not result:
            return "\nInvalid expression\n"
        evaluate_list = result

    while "/" in evaluate_list:
        result = pemd("/", evaluate_list)
        if not result:
            return "\nInvalid expression\n"
        evaluate_list = result
    
    i = 0
    while True:
        if evaluate_list[i] == "+":
            evaluate_list = pemd("+", evaluate_list)
            i = 0
        elif evaluate_list[i] == "-":
            evaluate_list = pemd("-", evaluate_list)
            i = 0
        else:
            i += 1
        
        if "+" not in evaluate_list and "-" not in evaluate_list:
            break
    
    return round(evaluate_list[0], 4)

while True:
    user = input("Type an expression\n>")
    user = validate(user)
    
    if not user:
        print("\nInvalid expression\n")
        continue
    
    terms, operators = parse(user)
    print(evaluate(terms, operators))
