from pathlib import Path


def print_words_reverse(words_list, index):
    if index < 0:
        return
    else:
        print(words_list[index], end=" ")
        print_words_reverse(words_list, index - 1)

def main():
    try:
        # Prompt the user for the file name
        #filename = input("Enter a filename: ")
        filepath = Path(__file__).parent / "JackAndJill.txt"
        # Read the file into a list of words
        with open(filepath, 'r') as file:
            words = file.read().split()

        # Call the recursive function to print words in reverse order
        print("Words in reverse order:")
        print_words_reverse(words, len(words) - 1)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
