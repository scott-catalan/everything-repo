in1 = int(input("Type any whole number: "))
div = 2

def PrimeNumber():
    global div
    if in1 <= 1:
        print(str(in1) + " is not prime.")
        return
    while div < in1:
        if in1 % div == 0:
            print(str(in1) + " is not prime.")
            return
        div += 1
    print(str(in1) + " is prime.")

PrimeNumber()