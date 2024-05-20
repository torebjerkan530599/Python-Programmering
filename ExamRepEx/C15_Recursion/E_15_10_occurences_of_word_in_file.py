from pathlib import Path


def countWords(words, word, count):
    if not words:
        return count
    else:
        if words[0] == word:
            count += 1
        return countWords(words[1:], word, count)

def main():
    try:
        # Prompt the user for the file name
        #filename = input("Enter a filename: ")
        filepath = Path(__file__).parent / "JackAndJill.txt"

        # Read the file into a list of words
        with open(filepath, 'r') as file:
            words = file.read().split()

        # Prompt the user for the word to find
        word = input("Enter a word: ")

        # Count the occurrences of the word using the recursive function
        count = countWords(words, word, 0)

        # Display the number of occurrences of the word
        print(f"{word} appears {count} times in the file.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
