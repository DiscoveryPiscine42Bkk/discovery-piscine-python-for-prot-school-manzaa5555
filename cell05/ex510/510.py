import sys

def main():
    if len(sys.argv) == 2:
        parameter = sys.argv[1]

        user_input = input("ป้อนคำ: ")

        if user_input == parameter:
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")

if __name__ == "__main__":
    main()