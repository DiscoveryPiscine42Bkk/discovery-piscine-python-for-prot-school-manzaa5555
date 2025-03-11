def main():
    try:
        num_str = input("ป้อนตัวเลข: ")

        if "." in num_str:
            print("ตัวเลขนี้เป็นทศนิยม")
        else:
            print("ตัวเลขนี้ไม่ใช่ทศนิยม")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    main()