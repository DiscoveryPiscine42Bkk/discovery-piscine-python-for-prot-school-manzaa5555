def upcase_it(input_string):
    """แปลงสตริงเป็นตัวพิมพ์ใหญ่และคืนค่า"""
    return input_string.upper()

def main():
    result = upcase_it('hello')
    print(result)

if __name__ == "__main__":
    main()