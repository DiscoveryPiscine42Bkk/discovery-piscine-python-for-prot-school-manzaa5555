def main():

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    filtered_array = [num for num in original_array if num > 5]

    print(filtered_array)

if __name__ == "__main__":
    main()