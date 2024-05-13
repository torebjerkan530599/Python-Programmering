list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Using zip to combine two lists into a list of tuples
zipped = zip(list1, list2)

# Result: [(1, 'a'), (2, 'b'), (3, 'c')]
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']

zipped = zip(list1, list2, list3)
#print(*zipped)
# Result: [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]


# If you need to unzip the result back into separate lists, 
# you can use the * operator to unpack the tuples:
unzipped = list(zip(*zipped))
print(unzipped)
# Result:
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = ['x', 'y', 'z']
