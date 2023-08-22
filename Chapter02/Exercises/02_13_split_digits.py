
number = int(input("Enter an integer: "))
lastDigit = number % 10 # isolate last digit in number
print(lastDigit)

number = number // 10 # remove last digit
lastDigit = number % 10
print(lastDigit)

number = number // 10
lastDigit = number % 10
print(lastDigit)

number = number // 10
lastDigit = number % 10
print(lastDigit)
