import math

def main():
    try:
        num = float(input("ป้อนตัวเลข: "))

        rounded_up = math.ceil(num)

        print(f"ตัวเลข {num} ปัดเศษขึ้นเป็น {rounded_up}")

    except ValueError:
        print("Error: โปรดป้อนตัวเลขเท่านั้น")

if __name__ == "__main__":
    main()