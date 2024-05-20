from random import randint
import os.path

def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    if os.path.isfile(f1):
        print("The file already exists")
        return
    
    # Open files for output 
    outputFile = open(f1, "w")
    
    for i in range(100):
        print(randint(0, 999), file = outputFile, end = " ")
    
    outputFile.close()
    
    inputFile = open(f1, "r")
    s = inputFile.read() # Read all from the file

    numbers = [int(items) for items in s.split()]
    numbers.sort()
    
    for i in range(len(numbers)):
        print(numbers[i], end = " ")
        
    inputFile.close() # Close the output file

main()
