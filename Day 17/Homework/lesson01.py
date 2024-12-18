def main():
    print("Welcome! Let's collect some numbers.")


    first_number = input("Enter the first number: ")


    numbers = [first_number]


    while True:
        next_number = input("Enter another number (or type 'done' to finish): ")

        if next_number.lower() == 'done':
            break
        
        numbers.append(next_number)


    print(f"You entered {len(numbers)} numbers.")

if __name__ == "__main__":
    main()
