# (Financial application: calculate future investment value)
# Write a program that reads in an investment amount, the annual interest rate, and the number of years, 
# and then displays the future investment value using the following formula:
# futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ^ numberOfMonths
# For example, if you enter the amount 1000.56, an annual interest rate of 4.25%, 
# and the number of years as 1, the future investment value is 1043.33. 

investmentAmount = float(input("Enter investment amount: "))
annualInterest = float(input("Enter annual interest rate: "))
years = int(input("Enter number of years: "))

numberOfMonths = years * 12

monthlyInterestRate = (annualInterest / numberOfMonths) / 100

futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths

print("Accumulated value is", float(f'{futureInvestmentAmount:.2f}'))

print("Accumulated value is", futureInvestmentAmount)

# 1043.92 = 1000.56 * (1 + 0.08333333333) ^ x  , x is 0.53002...