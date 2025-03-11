#!/usr/bin/env python3

def main():
    try:
        # รับอินพุตจากผู้ใช้และแปลงเป็นจำนวนเต็ม
        user_input = int(input("ป้อนตัวเลข: "))

        # ตรวจสอบว่าอินพุตน้อยกว่าหรือเท่ากับ 25
        if user_input <= 25:
            # วนลูปและแสดงตัวเลขจากอินพุตถึง 25
            for i in range(user_input, 26):
                print(i)
        else:
            # แสดงข้อผิดพลาดหากอินพุตมากกว่า 25
            print("Error")

    except ValueError:
        # จัดการกรณีที่อินพุตไม่ใช่จำนวนเต็ม
        print("Error: โปรดป้อนตัวเลขเท่านั้น")

if __name__ == "__main__":
    main()