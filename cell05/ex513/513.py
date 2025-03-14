import sys

def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if not sys.argv[i].endswith("ism"):
                print(sys.argv[i] + "ism")
    else:
        print("none")

if __name__ == "__main__":
    main()