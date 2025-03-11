
def main():
    try:
        age = int(input("ป้อนอายุของคุณ: "))

        age_plus_10 = age + 10
        age_plus_20 = age + 20
        age_plus_30 = age + 30

        print(f"ในอีก 10 ปี คุณจะมีอายุ {age_plus_10} ปี")
        print(f"ในอีก 20 ปี คุณจะมีอายุ {age_plus_20} ปี")
        print(f"ในอีก 30 ปี คุณจะมีอายุ {age_plus_30} ปี")

    except ValueError:
        print("Error: โปรดป้อนตัวเลขเท่านั้น")

if __name__ == "__main__":
    main()