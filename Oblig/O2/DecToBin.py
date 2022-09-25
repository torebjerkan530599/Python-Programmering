# Liang 4.7 Write a program that prompts 
# the user to enter a decimal number between 
# 0 and 15 and displays its corresponding binary value

num = int(input("Enter a number [0, 15]: "))

s1 = ""

if (num >= 0 and num <= 15 )  :
    q1 = num / 2
    rem1 = int(num % 2)

    q2 =  q1/ 2
    rem2 = int(q1 % 2)

    q3 = q2 / 2
    rem3 = int(q2 % 2)

    q4 =  q3 / 2
    rem4 = int(q3 % 2)

    s1 = str(rem4) + str(rem3) + str(rem2) + str(rem1)
    print(s1)
else:
    print("Not a valid number")


