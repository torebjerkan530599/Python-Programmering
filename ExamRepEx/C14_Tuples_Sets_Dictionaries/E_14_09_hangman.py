from pathlib import Path
import random

# Replace punctuations in the line with space
def replacePunctuations(line):
    for ch in line:
        if ch in '~@#$%^&*()_\'-+=~"<>?/,.;!{}[]|':
            line = line.replace(ch, "")
    return line

# get a random word from a file
filepath = Path(__file__).parent / "JackAndJill.txt"
with open(filepath,'r') as file:
    # text = replacePunctuations(file.read().split())
    # print(len(text))
    for line in file:
        content = replacePunctuations(line).lower()
        words = content.split()
        #print(words)

    index = random.randint(0,len(words)-1)
    word = words[index]


word_dict = {k: v for k,v in enumerate(word)}
mask = ['*'] * len(word)
#print('word is: ' + word) for testing purposes
print('Each time you guess a correct letter you get a free try!')
print(*mask)

tries = len(word)
correct_guess = False

print('word is: ' + word)

#for k,v in word_dict.items():
while tries > 0:
    print(f'Tries left: {tries}')    
    letter = input('guess a letter in the secret word: ')
    
    if letter in word:
        for i in range(len(word)):
            if word_dict[i] == letter:
                mask[i] = letter
        if ''.join(mask) == word:
            #print("Congratulations!!")
            correct_guess = True
            break
    else:
        tries -= 1
    
    print(*mask)
    
if correct_guess:
    print("Congratulations!!")
else:
    print('You gonna hang!')

print('Word was: ' + word)

