#file_name = input('Enter a filename:')

# a dictionary with values as a set will look like this:
# d = {key:(value1, value2, value3)}

file_name = 'initials.txt'

file = open(file_name,'r')
text = file.read().split()
file.close()
word_dict = {}

for word in text:
    initial = word[0]
    if initial not in word_dict:
        word_dict[word[0]] = set()
    word_dict[initial].add(word)


sorted_dict = sorted(word_dict.items())

for k,v in sorted_dict:
     print(k)
     print(f'\t {", ".join(str(e) for e in v)}')
    


