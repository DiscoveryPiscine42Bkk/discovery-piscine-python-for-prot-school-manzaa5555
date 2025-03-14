import sys

def shrink(input_string):
    """แสดง 8 ตัวอักษรแรกของสตริง"""
    print(input_string[:8])

def enlarge(input_string):
    """ต่อท้าย 'Z' จนครบ 8 ตัวอักษรและแสดงผล"""
    print(input_string + 'Z' * (8 - len(input_string)))

def main():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if len(sys.argv[i]) > 8:
                shrink(sys.argv[i])
            elif len(sys.argv[i]) < 8:
                enlarge(sys.argv[i])
            else:
                print(sys.argv[i])
    else:
        print("none")

if __name__ == "__main__":
    main()