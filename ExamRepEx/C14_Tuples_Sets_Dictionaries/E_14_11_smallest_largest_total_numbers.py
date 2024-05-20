# Prompt the user to enter 10 whole numbers and store them in a set
numbers_set = set()
for i in range(10):
    number = int(input("Please enter a whole number: "))
    numbers_set.add(number)

# Find the smallest, largest, and sum of all numbers entered
smallest = min(numbers_set)
largest = max(numbers_set)
total = sum(numbers_set)

# Display the results
print(f"The smallest number you entered was: {smallest}")
print(f"The largest number you entered was: {largest}")
print(f"The sum of all numbers you entered was: {total}")
