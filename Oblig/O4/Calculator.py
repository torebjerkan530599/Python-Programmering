from tkinter import * # Import tkinter

class Calculator:
    
    def __init__(self):
        self.__window = Tk()
        self.__window.geometry("300x400")
        self.__window.resizable(False,False)
        self.__window.title("Calculator GUI")
        self.__log = []
        self.__logOutputText = 'Log:'
        
        self.__inputFrame = Frame(self.__window, padx=5,pady=5, borderwidth=2, highlightthickness=1, highlightbackground="black")
        self.__inputFrame.pack(fill='x', padx = 10)
        #self.__inputFrame.grid(row=1,column=1)
        lblOp1 = Label(self.__inputFrame, text = "Operand 1")
        lblOpe = Label(self.__inputFrame, text = "Operator (+-*/) ")
        lblOp2 = Label(self.__inputFrame, text = "Operand 2")
        lblResult = Label(self.__inputFrame, text = "Result   ")
        
        lblOp1.grid(row = 1, 
            column = 1, sticky = W)
        lblOpe.grid(row = 2, 
            column = 1, sticky = W)
        lblOp2.grid(row = 3, 
            column = 1, sticky = W)
        lblResult.grid(row = 4, 
            column = 1, sticky = W)
        
        self.__operand1 = StringVar()
        eOp1 = Entry(self.__inputFrame, textvariable = self.__operand1, 
            justify = RIGHT)
        
        self.__operand2 = StringVar()
        eOp2 = Entry(self.__inputFrame, textvariable = self.__operand2, 
            justify = RIGHT)
        
        self.__operator = StringVar()
        eOpe = Entry(self.__inputFrame, textvariable = self.__operator, 
            justify = RIGHT)

        self.__resultVar = StringVar(self.__inputFrame, '0', "output")
        self.__outResult = Label(self.__inputFrame, textvariable = self.__resultVar)
        self.__outResult.grid(row = 4, column = 2, sticky=W)
         
        eOp1.grid(row = 1, column = 3)
        eOpe.grid(row = 2, column = 3)
        eOp2.grid(row = 3, column = 3)
        
        self.__btCalculate = Button(self.__inputFrame, text = "Calculate", command = lambda: self.calculate(self.__operand1, self.__operand2, self.__operator))
        self.__btClear = Button(self.__inputFrame, text = "Clear", command= self.clear_log)
        self.__btQuit = Button(self.__inputFrame, text = 'Quit', command= self.quit)
        self.__btCalculate.grid(row = 5, column=1, sticky="e")
        self.__btClear.grid(row = 5, column=2, sticky="w")
        self.__btQuit.grid(row = 5, column = 3, sticky= "w")

        self.outputFrame = Frame(self.__window, highlightthickness=1, highlightbackground="black")
        #self.outputFrame.grid(row=2,column=1)
        self.outputFrame.pack(fill='x', padx = 10, pady=10)
        self.__logArea = Canvas( self.outputFrame, bg = "white")
        #self.__logArea.grid(row = 6, column=1)
        self.__logArea.pack()
        self.__logArea.create_text(10, 10, text= "Log:", fill="black", font=('Helvetica 10'), anchor= NW, justify='left')

        self.__window.mainloop() # Create an event loop
    
    def get_log(self):
        if(self.__log):
            return '\n'.join(self.__log)
         
    def get_last_logged(self):
        if(self.__log):
            return self.__log[-1]
        
    def clear_log(self):
        self.__logArea.delete('all')
        self.__log.clear()
        self.__logArea.create_text(10, 10, text= "Log:", fill="black", font=('Helvetica 10'), anchor= NW, justify='left')
    
    def calculate(self, operand1, operand2,operator):
        result = 0
        # call from code (i.e. testcode in assignment)
        if(isinstance(operator,str)): 
            op = {  '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y}
            result = op[operator](operand1,operand2)
            self.__log.append(f'{operand1} {operator} {operand2} = { format(round(result, 2),".2f")}')
         # event triggered by widget
        else:    
            result = eval(operand1.get()+operator.get()+operand2.get())
            self.__resultVar.set(str(format(round(result, 2),".2f"))) # format it
            
            self.__log.append(f'{operand1.get()} {operator.get()} {operand2.get()} = { format(round(result, 2),".2f")}')
            nl = '\n'
            self.__logOutputText = f"Log:{nl}{nl.join(self.__log)}"
            self.__logArea.delete('all')
            self.__logArea.create_text(10, 10, text= self.__logOutputText, fill="black", font=('Helvetica 10'), anchor= NW, justify='left')
            return result
        
    def quit(self):
        self.__window.destroy() # if I want to printout testcode in assignment
        # quit() 
        return
            
# if __name__ == "__main__":
#     calculator = Calculator()
#     calculator.calculate(1,2,'+')
#     calculator.calculate(2,2,'*')
#     calculator.calculate(16,2,'/')
#     print(calculator.get_log())
#     print(calculator.get_last_logged())