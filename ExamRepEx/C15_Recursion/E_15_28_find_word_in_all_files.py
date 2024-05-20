import os

def search_word_in_files(directory, word):
    # Traverse the directory recursively
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # Construct the full path of the file
            file_path = os.path.join(root, file_name)
            try:
                # Open the file for reading
                with open(file_path, 'r') as file:
                    # Read lines from the file
                    lines = file.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        # Check if the word exists in the line
                        if word in line:
                            print(f"Found '{word}' in '{file_path}' (Line {line_number}): {line.strip()}")
            except IOError as e:
                print(f"Error reading file '{file_path}': {e}")

def main():
    # Prompt the user to enter a directory name and a word
    directory = input("Enter the directory name: ")
    word = input("Enter the word to search for: ")

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    # Search for the word in all files under the directory
    search_word_in_files(directory, word)

if __name__ == "__main__":
    main()
