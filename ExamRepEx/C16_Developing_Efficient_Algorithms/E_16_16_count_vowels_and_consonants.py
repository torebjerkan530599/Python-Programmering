def count_vowels_and_consonants(s):
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    unique_vowels = set()
    unique_consonants = set()
    
    # Convert the string to lowercase to make the process case-insensitive
    s = s.lower()
    
    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels_set:
                unique_vowels.add(char)
            else:
                unique_consonants.add(char)
    
    # The number of unique vowels and consonants
    num_unique_vowels = len(unique_vowels)
    num_unique_consonants = len(unique_consonants)
    
    print(f"Number of unique vowels: {num_unique_vowels}")
    print(f"Number of unique consonants: {num_unique_consonants}")

# Prompt the user to enter a string
user_input = 'Welcome to Python'#input("Enter a string: ")
count_vowels_and_consonants(user_input)
