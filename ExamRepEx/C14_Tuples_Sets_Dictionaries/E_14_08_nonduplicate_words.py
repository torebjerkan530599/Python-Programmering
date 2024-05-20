from pathlib import Path


def main():
    # Prompt the user to enter filenames
    f1 = Path(__file__).parent / "JackAndJill.txt"
    #f1 = input("Enter a filename: ").strip()

    # Open files for input 
    inputFile = open(f1, "r")
    
    s = inputFile.read() # Read all from the file
    inputFile.close()
    
    words = s.split()
    nonduplicateWords = set(words)
    words = list(nonduplicateWords)
    words.sort()
    
    for word in words:
        print(word, end = " ") 

main()
