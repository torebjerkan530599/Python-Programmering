from tkinter import * # Import tkinter

class Calculator:
    
    def __init__(self):
        self.__window = Tk()
        self.__window.rowconfigure(0,weight=1)
        self.__window.columnconfigure(0,weight=1)
        self.__window.resizable(False,False)
        self.__window.title("Calculator GUI")
        self.__log = []
        self.__logOutputText = ''
        
        self.__inputFrame = Frame(self.__window, width=200,height=200, padx=5,pady=5, borderwidth=1, highlightthickness=1, highlightbackground="black")
        self.__inputFrame.grid(row=1,column=1)
        lblOp1 = Label(self.__inputFrame, text = "Operand 1")
        lblOpe = Label(self.__inputFrame, text = "Operator ")
        lblOp2 = Label(self.__inputFrame, text = "Operand 2")
        lblResult = Label(self.__inputFrame, text = "Result   ")
        
        lblOp1.grid(row = 1, 
            column = 1, sticky = W)
        lblOpe.grid(row = 2, 
            column = 1, sticky = W)
        lblOp2.grid(row = 3, 
            column = 1, sticky = W)
        lblResult.grid(row = 5, 
            column = 1, sticky = W)
        
        self.__operand1 = StringVar()
        eOp1 = Entry(self.__inputFrame, textvariable = self.__operand1, 
            justify = RIGHT)
        
        self.__operator = StringVar()
        eOpe = Entry(self.__inputFrame, textvariable = self.__operator, 
            justify = RIGHT)
        
        self.__operand2 = StringVar()
        eOp2 = Entry(self.__inputFrame, textvariable = self.__operand2, 
            justify = RIGHT)

        self.__resultVar = StringVar(self.__inputFrame, '0', "output")
        self.__outResult = Label(self.__inputFrame, textvariable = self.__resultVar)
        self.__outResult.grid(row = 5, column = 2, sticky=W)
         
        eOp1.grid(row = 1, column = 3)
        eOpe.grid(row = 2, column = 3)
        eOp2.grid(row = 3, column = 3)
        
        self.__btCalculate = Button(self.__inputFrame, text = "Calculate", command = self.calculate)
        self.__btClear = Button(self.__inputFrame, text = "Clear", command= self.clear_log)
        self.__btQuit = Button(self.__inputFrame, text = 'Quit', command= self.quit)
        self.__btCalculate.grid(row = 4, column=1)
        self.__btClear.grid(row = 4, column=2, sticky="w")
        self.__btQuit.grid(row = 4, column = 3, sticky= "w")

        self.__logArea = Canvas(self.__window, width=200,height=200, bg = "white")
        self.__logArea.grid(row = 6, column=1)

        self.__window.mainloop() # Create an event loop
    
    def get_log(self):
        return '\n'.join(self.__log)
         
    def get_last_logged(self):
        return self.__log[-1]
        
    def clear_log(self):
        self.__logArea.delete('all')
        self.__log.clear()
    
    def calculate(self):
        result = 0
        if(self.__operator.get() == '+'):
            result = float(self.__operand1.get()) + float(self.__operand2.get())
        if(self.__operator.get() == '-'):
            result = float(self.__operand1.get()) - float(self.__operand2.get())
        if(self.__operator.get() == '*'):
            result = float(self.__operand1.get()) * float(self.__operand2.get())
        if(self.__operator.get() == '/'):
            result = float(self.__operand1.get()) / float(self.__operand2.get())
        self.__resultVar.set(str(result))
        
        self.__log.append(f'{self.__operand1.get()} {self.__operator.get()} {self.__operand2.get()} = {result}')
        nl = '\n'
        self.__logOutputText = f"Log:{nl}{nl.join(self.__log)}"
        self.__logArea.delete('all')
        # print(self.__logOutputText)
        # print("last:" + self.get_last_logged())
        self.__logArea.create_text(50, 30, text= self.__logOutputText, fill="black", font=('Helvetica 10 bold'), anchor= N)
        return result
        
    def quit(self):
        exit()
        
Calculator()