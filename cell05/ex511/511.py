import sys

def main():
    if len(sys.argv) > 1:
        print(f"parameters: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"{sys.argv[i]} {len(sys.argv[i])}")
    else:
        print("none")

if __name__ == "__main__":
    main()