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
with open(filepath, 'r') as file:
    for line in file:
        content = replacePunctuations(line).lower()
        words = content.split()

# Select a random word from the list
word = random.choice(words)

# Initialize variables
word_dict = {k: v for k, v in enumerate(word)}
mask = ['*'] * len(word)
tries = len(word)
#print('word is: ' + word) for testing purposes
print('Each time you guess a correct letter you get a free try!')
print(*mask)



# Main game loop
correct_guess = False
while tries > 0:
    print(f'Tries left: {tries}')
    letter = input('Guess a letter in the secret word: ').lower()

    # Check if the guessed letter is in the word
    if letter in word:
        for i in range(len(word)):
            if word_dict[i] == letter:
                mask[i] = letter
        if ''.join(mask) == word:
            correct_guess = True
            break
    else:
        tries -= 1

    print(*mask)

# Check if the game is won or lost
if correct_guess:
    print("Congratulations!!")
else:
    print('You gonna hang!')

print('Word was: ' + word)

