# O2: Palindrome  (Liang 6.3)

from math import remainder
def reverse(number):
    reverse = 0 
    while(number != 0):
        remainder = number % 10 
        reverse = reverse * 10 + remainder
        number = int(number / 10)
    return reverse


# Return true if number is a palindrome
def isPalindrome(number):
    return reverse(number) == number
    
number = int(input("Enter a number to check if it is a palindrome: "))
if(isPalindrome(number)) :
    print("It is a palindrome")  
else :
    print("Not a palindrome")