

def main():

    user_input = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")

    try:
        
        numbers = [float(num.strip()) for num in user_input.split(',')]

    
        total_sum = sum(numbers)

    
        print(f"The sum of the numbers is: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by commas.")

if __name__ == "__main__":
    main()
