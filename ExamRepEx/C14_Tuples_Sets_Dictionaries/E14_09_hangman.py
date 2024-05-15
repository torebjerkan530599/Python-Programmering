import random

# Replace punctuations in the line with space
def replacePunctuations(line):
    for ch in line:
        if ch in '~@#$%^&*()_\'-+=~"<>?/,.;!{}[]|':
            line = line.replace(ch, "")
    return line

# get a random word from a file
with open('test.txt','r') as file:
    # text = replacePunctuations(file.read().split())
    # print(len(text))
    for line in file:
        content = replacePunctuations(line).lower()
        words = content.split()
        print(words)

    index = random.randint(0,len(words)-1)
    word = words[index]


word_dict = {k: v for k,v in enumerate(word)}
wordCounts = {} # Create an empty dictionary to count words

mask = ['*'] * len(word)
print('Each time you guess a correct letter you get a free try!')
print(*mask)

#print(len(word))
tries = len(word)
print('word is: ' + word)
for k,v in word_dict.items():
    print(f'Tries left: {tries-k}')    
    letter = input('guess a letter in the secret word: ')
    if letter in word_dict.values():
        for i in range(len(word)):
            if word_dict[i] == letter:
                mask[i] = letter
        if ''.join(mask) == word:
            print("Congratulations!!")
            break
        
    if k == len(word):
        print('You gonna hang!')
        break

    
    print(*mask)
print('word was: ' + word)

