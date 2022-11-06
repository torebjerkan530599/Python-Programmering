from tkinter import * # Import tkinter

class ProcessChoice:

    def __init__(self) -> None:
        window = Tk() # Create a root window
        window.title("Radio buttons and buttons") # Set title

        # Place buttons in frame
        rBtnframe = Frame(window)
        rBtnframe.pack()
        btnFrame = Frame(window)
        btnFrame.pack()

        self.__var = IntVar()

        self.__btRadioRed      = Radiobutton(rBtnframe, text = "Red", variable = self.__var, value =  1, command = self.changeColor)
        self.__btRadioYellow   = Radiobutton(rBtnframe, text = "Yellow", variable = self.__var, value =  2, command = self.changeColor)
        self.__btRadioWhite    = Radiobutton(rBtnframe, text = "White", variable = self.__var, value =  3, command = self.changeColor)
        self.__btRadioGray     = Radiobutton(rBtnframe, text = "Gray", variable = self.__var, value = 4, command = self.changeColor)
        self.__btRadioGreen    = Radiobutton(rBtnframe, text = "Green", variable = self.__var, value = 5, command = self.changeColor)

        self.__btRadioRed   .grid(row = 1, column = 1)
        self.__btRadioYellow.grid(row = 1, column = 2)
        self.__btRadioWhite .grid(row = 1, column = 3)
        self.__btRadioGray  .grid(row = 1, column = 4)
        self.__btRadioGreen .grid(row = 1, column = 5)

        self.__canvas = Canvas(rBtnframe, width = 200, height = 100, bg = "white") 
        self.__canvas.grid(row=2, column=1, columnspan=  5)
        
        self.__btLeft = Button(btnFrame, text = "<=")
        self.__btRight = Button(btnFrame, text = "=>")

        self.__btLeft.bind("<Button-1>", self.moveLeft)
        self.__btRight.bind("<Button-1>", self.moveRight)

        self.__btLeft.grid(row = 3, column = 1)
        self.__btRight.grid(row = 3, column = 2)

        self._dx = 3 # change in x from current x
        self.__canvas.create_text(100,50,text = "Welcome", font = "Times 10 bold underline", tags = "message")

        window.mainloop() # Create an event loop

    def changeColor(self):
        if self.__var.get() == 1:
           self.__canvas.configure(bg = "red")
        elif self.__var.get() == 2:
           self.__canvas.configure(bg = "yellow")
        elif self.__var.get() == 3:
           self.__canvas.configure(bg = "white")
        elif self.__var.get() == 4:
           self.__canvas.configure(bg = "grey")
        else:
           self.__canvas.configure(bg = "green")

    
    def moveLeft(self, event):
        self.__canvas.move("message", -self._dx, 0)
        self.__canvas.update()
         
    def moveRight(self, event):
        self.__canvas.move("message", self._dx, 0)
        self.__canvas.update()
    
        
ProcessChoice() # Create an object to invoke __init__ method