def find_longest_word(words):
    if len(words) == 1:
        return words[0]
    else:
        # Recursive call to find_longest_word with the sublist excluding the first word
        longest_in_rest = find_longest_word(words[1:])
        # Compare the length of the first word with the longest word found in the rest of the list
        if len(words[0]) >= len(longest_in_rest):
            return words[0]
        else:
            return longest_in_rest

def main():
    try:
        # Prompt the user to enter words separated by spaces
        words_input = input("Enter words separated by spaces on one line: ")
        words = words_input.split()
        
        # Find the longest word using the recursive function
        longest_word = find_longest_word(words)
        
        # Display the result
        print(f"The longest word in {words} is {longest_word}.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
