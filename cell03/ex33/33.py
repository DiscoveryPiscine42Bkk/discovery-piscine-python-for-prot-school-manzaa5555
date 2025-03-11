def main():
    for number in range(1, 13):
        print(f"ตารางสูตรคูณแม่ {number}:")
        for i in range(1, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
        print()  

if __name__ == "__main__":
    main()