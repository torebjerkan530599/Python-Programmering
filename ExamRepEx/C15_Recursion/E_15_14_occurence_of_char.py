def countCharacters(s, char):
    # to ignore case:
    # s = s.lower()
    # char = char.lower()
    # Initialize the recursion with the full length of the string minus one
    return countHelper(s, char, len(s) - 1)

def countHelper(s, char, high):
    # Base case: if the index is less than 0, return 0
    if high < 0:
        return 0
    # Check if the current character matches 'char' (case-sensitive) and count it
    count = 1 if s[high] == char else 0
    # Recursively count occurrences of 'char' in the rest of the string
    return count + countHelper(s, char, high - 1)

def main():
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")
    # Prompt the user to enter the character to count
    char_to_count = input("Enter a character: ")
    
    # Ensure only a single character is provided
    if len(char_to_count) != 1:
        print("Please enter a single character.")
        return
    
    # Count the occurrences of the specified character using the recursive function
    num_occurrences = countCharacters(user_input, char_to_count)
    
    # Display the result
    print(f"'{char_to_count}' appears {num_occurrences} times in '{user_input}'")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

