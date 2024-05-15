
# Maximum consecutive increasingly ordered substring
string = 'abcabcdgabxy'
max_substring = string[0]  # Initialize with the first character
current_substring = string[0]  # Initialize with the first character

for i in range(1, len(string)):
    if ord(string[i]) > ord(string[i - 1]):  # Check if current character is greater than the previous one
        current_substring += string[i]  # Extend the current substring
    else:
        if len(current_substring) > len(max_substring):
            max_substring = current_substring  # Update max_substring if current substring is longer
        current_substring = string[i]  # Start a new substring from the current character

# Check the last substring
if len(current_substring) > len(max_substring):
    max_substring = current_substring

print(max_substring)


# Maximum decreasingly ordered substring...TODO
    
    