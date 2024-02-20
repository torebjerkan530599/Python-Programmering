import os.path

file_name = input('Enter a filename:')
#file_name = 'initials.txt'

if os.path.isfile(file_name):
    file = open(file_name,'r')
    text = file.read().split()
    file.close()
else:
    print('File not found\n')

word_dict = {}

for word in text:
    initial = word[0]
    if initial not in word_dict:
        word_dict[word[0]] = set()
    word_dict[initial].add(word)

# option 1: make upper and lower-case appear next to eachother
sorted_list = list(word_dict.keys())
sorted_list.sort(key=lambda initial:initial.lower())
sorted_dict = {i: word_dict[i] for i in sorted_list}

# option 2: print all uppercase first then all lowercase
# sorted_dict = sorted(word_dict.items())
# for k,v in sorted_dict:
# ...

for k,v in sorted_dict.items():
    print(k)
    print(f'\t {", ".join(str(e) for e in v)}')
    


