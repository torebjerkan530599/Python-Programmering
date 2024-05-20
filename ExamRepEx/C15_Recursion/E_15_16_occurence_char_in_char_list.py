def count(chars, ch):
    return countHelper(chars, ch, len(chars) - 1)

def countHelper(chars, ch, high):
    if high < 0:
        return 0
    count = 1 if chars[high] == ch else 0
    return count + countHelper(chars, ch, high - 1)

def main():
    # Input characters separated by spaces
    char_list = ['A','b','u','D','h','a','b','i','B','a','y']
    #char_list = input("Enter characters separated by spaces from one line: ").split() # 
    # Input the character to count
    char_to_count = input("Enter a character: ")
    # Count the occurrences
    occurrences = count(char_list, char_to_count)
    # Display the result
    print(f"The number of occurrence of character {char_to_count} in {char_list} is {occurrences}")

if __name__ == "__main__":
    main()
