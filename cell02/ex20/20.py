number = input("enter a number: ")
try:
    num = int(number)
    if num == 0:
        print("this number is equal to zero.")
    else:
        print("this number is different from zero.")
except ValueError:
    print("inaslid input. plese enter a valid number.")