month = int(input("Enter a month in the year (e.g., 1 for Jan):")) 
year = int(input("Enter a year: "))
  # Check if the year is a leap year 

isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Display the result 
print(year, "is a leap year?", isLeapYear)

if(isLeapYear and month==2):
    print("29")
elif not isLeapYear and month==2:
    print("28")
elif (((month % 2 != 0) and (month < 8)) or ((month % 2 == 0) and (month > 7))): # jan, march, may, july
    print("31")
else:
    print("30")
