def main():
    try:
        num1 = float(input("ป้อนตัวเลขแรก: "))
        num2 = float(input("ป้อนตัวเลขที่สอง: "))

        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2


        print(f"{num1} + {num2} = {addition}")
        print(f"{num1} - {num2} = {subtraction}")
        print(f"{num1} * {num2} = {multiplication}")
        print(f"{num1} / {num2} = {division}")

    except ValueError:
        print("Error: โปรดป้อนตัวเลขเท่านั้น")
    except ZeroDivisionError:
        print("Error: ไม่สามารถหารด้วยศูนย์ได้")

if __name__ == "__main__":
    main()