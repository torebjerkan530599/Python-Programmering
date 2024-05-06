#NB! Difference between creating empty set and dictionary. Curly braces are used for both sets and dictionaries.

set1 = set() # to create empty set
set2 = {("A","B"),("C",)} # a set of two tuples

dict1 = {} # to create empty dictionary
dict2 = dict() # also to create empty dictionary
dict3 = {'A':("Ann","Albert"), 'B':("Bernard","Benny")} # a dict whose kets are characters and values are tuples 


# Accessing dictionaries

# returning value from entry with key "A"
print(dict3['A']) 
print(dict3.get('C')) # returns None if key doesn't exist
print(len(dict3))

print('B' in dict3)

# returning specific keys
first_key = list(dict3.keys())[0]
second_key = list(dict3.keys())[1]
print( first_key + " " + second_key)

dict4 = {("Peter", "Frampton"):5000, ("Joshua","Tree"): 2000, ("Cal",2): 10000}
first_key_second_value_in_tuple = tuple(dict4.keys())[0][1]
print(first_key_second_value_in_tuple)
last_key_second_value_in_tuple = tuple(dict4.keys())[len(dict4)-1][1]
print(last_key_second_value_in_tuple)



del dict4[("Cal",2)] # use del keyword to delete an entry
print(dict4)

#del dict4[min(dict4)] # to delete entry with smallest key
dict4.popitem()
print(f'After popitem: {dict4}') # popitem pops the last inserted item lifo (stack)
print(dict4.pop(tuple(dict4.keys())[0])) # to return a value and remove it at the same time use pop

print(dict4)


# test program
def main():
    # Prompt the user to enter a file
    filename = "test.txt" #input("Enter a filename: ").strip()
    inputFile = open(filename, "r") # Open the file

    wordCounts = {} # Create an empty dictionary to count words
    for line in inputFile:
        processLine(line.lower(), wordCounts)
    inputFile.close()
     
    pairs = list(wordCounts.items()) # Get pairs from the dictionary   

    items = [[count, word] for (word, count) in pairs] 
    items.sort(reverse = True) # Sort pairs in items
    
    for count, word in items[ : 10]: # Slice the first 10 items
        print(word, count, sep =  '\t')  
  
# Count each word in the line
def processLine(line, wordCounts): 
    line = replacePunctuation(line) # Replace punctuation with space
    words = line.split() # Get words from each line
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1 # Increase count for word
        else:
            wordCounts[word] = 1 # Add an item in the dictionary

# Replace punctuation in the line with space
def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line

main() # Call the main function