def find_min_recursive(numbers):
    # Base case: if the list contains only one number, return that number
    if len(numbers) == 1:
        return numbers[0]
    
    # Recursive case: compare the first number with the smallest of the rest of the list
    first = numbers[0]
    rest_min = find_min_recursive(numbers[1:])
    return first if first < rest_min else rest_min

def main():
    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter numbers separated by spaces from one line: ")
    
    # Convert the input string to a list of floats
    numbers = list(map(float, user_input.split())) # for test: 123 5 654 22 12 78 21 54 -2 15 53
    # Find the smallest number using the recursive function
    smallest_number = find_min_recursive(numbers)
    
    # Display the result
    print(f"The smallest number in {numbers} is {smallest_number}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
