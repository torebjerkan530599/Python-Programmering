with open('numbers.txt', 'r') as file:
    content = file.readline().split()
    numbers = sum(map(int, content))
    alternative = sum([int(x) for x in content]) # same as above
    average = numbers / len(content)
    print(alternative)
    print(numbers)
    print(average)


# other examples of map

# Python program to demonstrate working
# of map.
 
# Return double of n
def addition(n):
    return n + n
 
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# or simply
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result)) # must be converted

