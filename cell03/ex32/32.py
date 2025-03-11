def main():
    while True:
        user_input = input("ป้อนข้อความ (หรือ 'STOP' เพื่อหยุด): ")

        if user_input.upper() == "STOP":
            print("หยุดการทำงาน")
            break  

        print("ฉันเข้าใจแล้ว!")

if __name__ == "__main__":
    main()

