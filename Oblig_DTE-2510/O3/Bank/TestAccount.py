from Account import Account

account1 = Account(1, 1000, 50000, 7)
print(account1)
account1.deposit(500)
print(f'New balance after depositing 500 is {account1.getBalance()}')
account1.withdraw(1000)
print(f'New balance after withdrawal of 1000 is {account1.getBalance()}')
account1.showTransactions()