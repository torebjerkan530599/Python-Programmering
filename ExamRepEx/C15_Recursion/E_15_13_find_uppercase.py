def countUppercase(s):
    # Helper function to perform the recursive counting
    def countUppercaseHelper(s, high):
        # Base case: if the string is empty, return 0
        if high < 0:
            return 0
        # Check if the current character is uppercase and count it
        count = 1 if s[high].isupper() else 0
        # Recursively count uppercase letters in the rest of the string
        return count + countUppercaseHelper(s, high - 1)
    
    # Start the recursion with the full length of the string minus one
    return countUppercaseHelper(s, len(s) - 1)

def main():
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")
    
    # Count the number of uppercase letters using the recursive function
    num_uppercase = countUppercase(user_input)
    
    # Display the result
    print(f"The number of uppercase letters in '{user_input}' is {num_uppercase}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
