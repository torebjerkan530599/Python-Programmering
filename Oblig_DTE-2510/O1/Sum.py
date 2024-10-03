number = int(input("Enter an integer between 0 and 1000 (exclusive): "))
original_number = number

digit1 =  number % 10
number = number //10

digit2 =  number % 10
number = number //10

digit3 =  number % 10

sum = digit1 + digit2 + digit3

if(original_number > 0 and original_number < 1000):
    print("The sum of digits in", original_number , "is", sum)
else:
    print("The number is not between 0 and 1000")