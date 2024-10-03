month = int(input("Enter a month in the year (e.g., 1 for Jan):")) 
year = int(input("Enter a year: "))

# Check if the year is a leap year 
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(year, "is a leap year?", isLeapYear)

if(isLeapYear and month==2):
    print("29")
elif not isLeapYear and month==2:
    print("28")
elif (((month % 2 != 0) and (month < 8)) or ((month % 2 == 0) and (month > 7))):
    print("31")
else:
    print("30")
    
    '''Alternate solution From Revel
# Prompt the user to enter input
month = int(input("Enter a month in the year (e.g., 1 for Jan): "))

year = int(input("Enter a year: "))

numberOfDaysInMonth = 0;

if month == 1:
    print("January", year, end = "")
    numberOfDaysInMonth = 31;
elif month == 2:
    print("February", year, end = "")
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        numberOfDaysInMonth = 29;
    else:
        numberOfDaysInMonth = 28;
elif month == 3:
    print("March", year, end = "")
    numberOfDaysInMonth = 31;
elif month == 4:
    print("April", year, end = "")
    numberOfDaysInMonth = 30;
elif month == 5:
    print("May", year, end = "")
    numberOfDaysInMonth = 31;
elif month == 6:
    print("June", year, end = "")
    numberOfDaysInMonth = 30;
elif month == 7:
    print("July", year, end = "")
    numberOfDaysInMonth = 31;
elif month == 8:
    print("August", year, end = "")
    numberOfDaysInMonth = 31;
elif month == 9:
    print("September", year, end = "")
    numberOfDaysInMonth = 30;
elif month == 10:
    print("October", year, end = "")
    numberOfDaysInMonth = 31;
elif month == 11:
    print("November", year, end = "")
    numberOfDaysInMonth = 30;
else:
    print("December", year, end = "")
    numberOfDaysInMonth = 31;

print(" has", numberOfDaysInMonth, "days")

'''