from datetime import datetime
import string

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
    

