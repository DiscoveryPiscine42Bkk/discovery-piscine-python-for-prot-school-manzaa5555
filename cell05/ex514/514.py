import sys

def main():
    if len(sys.argv) == 23:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            my_range = list(range(start, end))

            print(my_range)

        except ValueError:
            print("Error: โปรดป้อนตัวเลขสองตัว")
    else:
        print("none")

if __name__ == "__main__":
    main()