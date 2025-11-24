import os

def takeinp():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter first number: "))
        return [a, b]
    except ValueError:
        print("Invalid value")

def add(val):
    return val[0]+val[1]

def sub(val):
    return val[0]-val[1]

def mul(val):
    return val[0]*val[1]

def div(val):
    try:
        return val[0]/val[1]
    except:
        print("Divide by zero error")

while True:
    match int(input('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Exit
Enter option: ''')):
        case 1:
            print("Addition: ", add(takeinp()))
            break
        case 2:
            print("Addition: ", sub(takeinp()))
            break
        case 3:
            print("Addition: ", mul(takeinp()))
            break
        case 4:
            print("Addition: ", div(takeinp()))
            break
        case 5:
            print("Addition: ", pow(int(input("Enter number"), int(input("Enter power: ")))))
            break
        case 6:
            exit
        case _:
            os.system("cls")
            print("Invalid operation")
    