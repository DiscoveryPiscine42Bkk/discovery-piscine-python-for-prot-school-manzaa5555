import sys

def downcase_it(input_string):
    """แปลงสตริงเป็นตัวพิมพ์เล็กและคืนค่า"""
    return input_string.lower()

def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            result = downcase_it(sys.argv[i])
            print(result)
    else:
        print("none")

if __name__ == "__main__":
    main()