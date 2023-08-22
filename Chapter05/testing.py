for i in range(1, 6 + 1):
    for j in range(6, 0, -1):
        print(j if j <= i else " ", end = " ")
    print()
    
    
investmentAmount = float(input("Enter investment amount: "))
annualInterest = float(input("Enter annual interest rate: "))
years = int(input("Enter number of years: "))

numberOfMonths = years * 12

monthlyInterestRate = (annualInterest / numberOfMonths) / 100

futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths

print("Accumulated value is", float(f'{futureInvestmentAmount:.2f}'))


# Exercise02_19
# Enter the investment amount
investmentAmount = float(input("Enter the investment amount, for example 120000.95: "))

# Enter yearly interest rate
annualInterestRate = float(input("Enter annual interest rate, for example 8.25: "))

# Obtain monthly interest rate
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numOfYears = int(input("Enter number of years as an integer, for example 5: "))

futureValue = investmentAmount * ((1 + monthlyInterestRate) ** (numOfYears * 12))

print("Future value is", int(futureValue * 100) / 100.0)