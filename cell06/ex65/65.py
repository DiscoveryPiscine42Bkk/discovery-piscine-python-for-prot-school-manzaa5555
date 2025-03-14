def add_one(num):
    """เพิ่ม 1 ให้กับตัวเลขที่รับมา"""
    num += 1
    print(f"ภายในฟังก์ชัน add_one: num = {num}")  

def main():
    my_var = 10
    print(f"ก่อนเรียกใช้ add_one: my_var = {my_var}")

    add_one(my_var)

    print(f"หลังเรียกใช้ add_one: my_var = {my_var}")

if __name__ == "__main__":
    main()