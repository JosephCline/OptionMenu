from math import sqrt as squareroot
def calculator(option):
    line = "-"
    if option == "CALCULATOR":
        print('')
        print(line * 45)
        print(
            "Enter addition for adding\n" "Enter subtraction for subtracting\n" "Enter multiplication for multiplying\n" "Enter division for dividing\n" "Enter squareroot to calculate squareroot\n" "Enter square to get the square of a number")
        print(line * 45)
    if option == "CALCULATOR":
        print('')
        print(line * 45)
        operator = input("Please enter an operator from above:\t")
        x = input("Please enter the first number:\t")
        y = input("Please enter the second number:\t")
    if option == "CALCULATOR" and operator == "addition":
        addition = float(x) + float(y)
        print(addition)
    elif option == "CALCULATOR" and operator == "subtraction":
        subtraction = float(x) - float(y)
        print(subtraction)
    elif option == "CALCULATOR" and operator == "multiplication":
        multiplication = float(x) * float(y)
        print(multiplication)
    elif option == "CALCULATOR" and operator == "division":
        division = float(x) / float(y)
        print(division)
    elif option == "CALCULATOR" and operator == "square":
        square = float(x) ** float(y)
        print(square)
    elif option == "CALCULATOR" and operator == "squareroot":
        squareroot_answer = float(squareroot(float(x)))
        print(squareroot_answer)
