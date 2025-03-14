def main():

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    filtered_array = [num for num in original_array if num > 5]

    unique_array = []
    for num in filtered_array:
        if num not in unique_array:
            unique_array.append(num)

    print(unique_array)

if __name__ == "__main__":
    main()