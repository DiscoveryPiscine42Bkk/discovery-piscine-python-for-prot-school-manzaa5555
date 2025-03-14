def greetings(name="noble stranger"):
    """แสดงข้อความต้อนรับพร้อมชื่อ"""
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

def main():
    greetings('Alexandra')
    greetings('Wil')
    greetings()
    greetings(42)

if __name__ == "__main__":
    main()