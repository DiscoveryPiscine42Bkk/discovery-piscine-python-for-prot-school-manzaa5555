import sys

def main():
    if len(sys.argv) > 2:
        for i in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[i])
    else:
        print("none")

if __name__ == "__main__":
    main()