# Process scores in a text file

# fileName = open(input("Enter filename with scores to be processed: "),"r")
# lst = fileName.read()
# print(lst)

with open("Numbers.txt","r") as file:
   nums = [int(x) for x in file.readline().split()]
   print(f'sum of {nums}: {sum(nums)}')
   print(f'average of {nums}: {sum(nums)/len(nums)}')
   print("T")
   print(file.readline())

# some extra trickery from chapter 13.2.5

counts = [0] * 26 # Alphabet

file = open("Presidents.txt","r")
for line in file:
    for ch in line.lower():
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
            
for i,count in enumerate(counts):
    print(chr(ord('a') + i) + " appears " + str(counts[i]))
    
