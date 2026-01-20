in1 = float(input("Type any number: "))

def ROUND():
    print("Your number's opposite is " + str(in1 * -1))
    print("Your number rounded to three decimals is " + str(round(in1, 3)))
    print("Your number's absolute value is " + str(abs(in1)))
    print("Your number in binary is " + str(bin(int(in1))))
    print("Your number in hexadecimal is " + str(hex(int(in1))))

ROUND()