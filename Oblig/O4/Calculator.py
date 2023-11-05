from tkinter import * # Import tkinter

class Calculator:
    
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Calculator GUI")
        self.__log = []
        # self.__operators = Frame(self.__window)
        
        # self.__var = IntVar()
        # self.__btRadioAdd      = Radiobutton(self.__operators, text = "+", variable = self.__var, value =  1, command = self.changeColor) # change to lambda by calling (operand1+operand2)
        # self.__btRadioSubtract = Radiobutton(self.__operators, text = "-", variable = self.__var, value =  2, command = self.changeColor)
        # self.__btRadioMultipy  = Radiobutton(self.__operators, text = "*", variable = self.__var, value =  3, command = self.changeColor)
        # self.__btRadioDivide   = Radiobutton(self.__operators, text = "/", variable = self.__var, value = 4, command = self.changeColor)
        
        self.__testFrame = Frame(self.__window, width=200, height=200, padx=5,pady=5, bd=1, highlightthickness=1, highlightbackground="black")
        self.__testFrame.grid(row=1,column=1)
        lblOp1 = Label(self.__testFrame, text = "Operand 1")
        lblOpe = Label(self.__testFrame, text = "Operator ")
        lblOp2 = Label(self.__testFrame, text = "Operand 2")
        result = Label(self.__testFrame, text = "Result   ")
        
        lblOp1.grid(row = 1, 
            column = 1, sticky = W)
        lblOpe.grid(row = 2, 
            column = 1, sticky = W)
        lblOp2.grid(row = 3, 
            column = 1, sticky = W)
        result.grid(row = 4, 
            column = 1, sticky = W)
        
        self.__operand1 = StringVar()
        eOp1 = Entry(self.__testFrame, textvariable = self.__operand1, 
            justify = RIGHT)
        
        self.__operator = StringVar()
        eOpe = Entry(self.__testFrame, textvariable = self.__operator, 
            justify = RIGHT)
        
        self.__operand2 = StringVar()
        eOp2 = Entry(self.__testFrame, textvariable = self.__operand2, 
            justify = RIGHT)
         
        eOp1.grid(row = 1, column = 2)
        eOpe.grid(row = 2, column = 2)
        eOp2.grid(row = 3, column = 2)

        self.__logArea = Canvas(self.__window, width = 200, height = 200, bg = "white", bd= 1 , highlightthickness=1, highlightbackground="black") #, bd= 1 , highlightthickness=1, highlightbackground="black"
        self.__logArea.grid(column=1, row = 5, columnspan=  2, padx= 5, pady= 5)
        self.__logArea.create_text(50, 10, text= self.get_log(), fill="black", font=('Helvetica 10 bold'))

        self.__btCalculate = Button(self.__testFrame, text = "Calculate", command = lambda o1=self.__operand1, o= self.__operator,  
                                o2=self.__operand2 : self.calculate(o1,o,o2))
        self.__btClear = Button(self.__testFrame, text = "Clear")
        self.__btCalculate.grid(row = 5, column=1)
        self.__btClear.grid(row = 5, column=2) 
                
        self.__window.mainloop() # Create an event loop
        
        
        
    def calculate(self,operand1,operand2,operator):
        result = 0
        if(operator == '+'):
            result = operand1 + operand2
        if(operator == '-'):
            result = operand1 - operand2
        if(operator == '*'):
            result = operand1 * operand2
        if(operator == '/'):
            result = operand1 / operand2
        
        self.__log.append(f'{operand1} operator {operand2} = {result}\n')
        return result

    def get_log(self):
        return ' '.join(self.__log)
         
    def get_last_logged(self):
        return self.__log[-1]
        
    def clear_log(self):
        self.__log.clear()
        
Calculator()