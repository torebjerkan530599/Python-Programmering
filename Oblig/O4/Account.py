import string

class Account:

    def __init__(self, custID, accountNo, balance, interest) -> None:
        self.__custID = custID
        self.__account = accountNo
        self.__balance = balance
        self.__interest = interest
        self.__transactions = []
        #self.__transactions = list(Transaction)

    def getBalance(self) -> float: 
        return self.__balance
    
    def deposit(self, amount) -> float:
        if amount > 0 :
            self.__transactions.append(Transaction(amount))
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount) -> float:
        self.__transactions.append(Transaction(-amount))
        if self.__balance > amount:
            self.__balance -= amount
        return self.__balance

    def showTransactions(self):
        print("\nTransactions: ")
        for t in self.__transactions:
            print(
                f'Time      :  {t.getTime()}\n'
                f'Amount    :  {t.getAmount()}\n')
            
    
    def __str__(self) -> string:
        return (
                f'Customer ID: {self.__custID}  \n'
                f'Account    : {self.__account} \n'
                f'Balance    : {self.__balance} \n'
                f'Interest   : {self.__interest}\n')

from datetime import datetime

class Transaction:

    def __init__(self,amount) -> None:
        self.__amount = amount
        self.__time = datetime.now()

    def __getTimeAsStr(self) -> string:
        self.__time = self.__time.strftime("%m-%d-%Y, %H:%M:%S")
        return self.__time
       
    def getTime(self):
        #return self.__time
        return self.__getTimeAsStr()
   
    def getAmount(self) -> float:
     return self.__amount
    
    def __str__(self):
        return (
            f'Time       : {self.getTime()}  \n'
            f'Amount     : {self.getAmount()} \n'
        )
    

    