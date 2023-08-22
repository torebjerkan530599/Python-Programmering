# (Find the number of years and days) 
# Write a program that prompts the user to enter the minutes (e.g., 1 billion), 
# and displays the number of years and days for the minutes. 
# For simplicity, assume a year has 365 days. Here is a sample run:
# Enter the number of minutes: 1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
#
#
#
#
import time

currentTime = time.time()
print("currentTime:", currentTime)
totalSeconds = int(currentTime)
print("totalSeconds", totalSeconds)

minutes = int(input("Enter the number of minutes: "));

#compute hours
hours = minutes // 60

#compute total days
totalDays = hours // 24

#compyte years
years = totalDays // 365

#remaining days
remainingDays = totalDays % 365



print(minutes, " minutes is approximately ", years, " years and ", remainingDays, " days ")

#1000000000