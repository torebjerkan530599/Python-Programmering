number = int(input("Enter an 3 digit integer: "))

digit1 =  number % 10
number = number //10

digit2 =  number % 10
number = number //10

digit3 =  number % 10

print("number is a palindrome" if digit1==digit3 else "not a palindrome")
    