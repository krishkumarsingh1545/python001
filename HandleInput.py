while True:
    try:
        a = int(input("Enter integer: "))
        print(float(a))
        break
    except:
        print("Invalid input")