# tuples are fixed and immutable!! But unlike sets they can have duplicate elements!

tuple1 = ("green", "red", "blue") # Create a tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5]) # Create a tuple from a list, # tuple(list) also possible
print(tuple2)

print("length is", len(tuple2)) # Use function len
print("max is", max(tuple2)) # Use max
print("min is", min(tuple2)) # Use min
print("sum is", sum(tuple2)) # Use sum

print("The first element is", tuple2[0]) # Use indexer

tuple3 = tuple1 + tuple2 # Combine 2 tuples
print(tuple3)

tuple3 = 2 * tuple1 # Multiple a tuple
print(tuple3)

print(tuple2[2 : 4]) # Slicing operator
print(tuple1[-1])

print(2 in tuple2) # in operator

for v in tuple1:
    print(v, end = " ")
print()
    
list1 = list(tuple2) # Obtain a list from a tuple
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5) # Compare two tuples
t6 = (1,2)
t7 = (2,1)

print(type(t6))
print(t6==t7) # because order matters in tuples

t = (1, 2, 3, 7, 9, 0, 5)
print(t)
print(t[0])
print(t[1 : 3])
print(t[-1])
print(t[ : -1])
print(t[1 : -1])
print(max(t))
print(min(t))
print(sum(t))
print(len(t))
t1 = (1, 2, 3, 7, 9, 0, 5)
t2 = (1, 3, 22, 7, 9, 0, 5)
print(t1 == t2)
print(t1 != t2)
print(t1 > t2)
print(t1 < t2)

t = () # simplest statement for creating a tuple

# how many times does the first element occur in the rest of the list?
t =(1,6,5,7,1,3,4,1)

repeats = 0
if t:
    first_element = t[0]
    index = 1
    while len(t) > index:
        if t[index] == first_element:
            repeats += 1
        index += 1
print(repeats)