def main():
    try:
        number = int(input("ป้อนตัวเลขสำหรับตารางสูตรคูณ: "))

        print(f"ตารางสูตรคูณของ {number}:")
        for i in range(1, 12):
            result = number * i
            print(f"{number} x {i} = {result}")

    except ValueError:
        print("Error: โปรดป้อนตัวเลขเท่านั้น")

if __name__ == "__main__":
    main()