from tkinter import *

class MoveBall():

    def __init__(self) -> None:
        self.window = Tk() # Create a root window
        self.window.title("Moving Ball") # Set title

        ballArea = Frame(self.window)
        btnframe = Frame(self.window)
        ballArea.pack(padx = 5, pady= 5, side=TOP)
        btnframe.pack(padx = 5, pady= 5, side=BOTTOM, fill=None)

        #variables for bounding box of the canvas in center of the screen
        self.xTopLeft = 0
        self.yTopLeft = 0
        self.xBottomRight = 0
        self.yBottomRight = 0

        self.canvas = Canvas(ballArea, width = 400, height = 200, bg = "white" , bd= 1 , highlightthickness=1, highlightbackground="black")
        self.canvas.pack(side=TOP, fill=X, expand=False)
        self.oval = self.canvas.create_oval(100, 50, 150, 100, fill = "red", tags="circle")
        
        btnLeft  = Button(btnframe, text = "Left" , command = lambda dx=-10, dy= 0 : self.moveBall(dx,dy))
        btnUp    = Button(btnframe, text = "Up"   , command = lambda dx= 0, dy=-10 : self.moveBall(dx,dy))    
        btnDown  = Button(btnframe, text = "Down" , command = lambda dx= 0, dy= 10 : self.moveBall(dx,dy))   
        btnRight = Button(btnframe, text = "Right", command = lambda dx= 10, dy= 0 : self.moveBall(dx,dy))

        btnLeft .pack(side=LEFT)
        btnUp   .pack(side=LEFT)
        btnDown .pack(side=LEFT)
        btnRight.pack(side=LEFT)

        self.centerWindow()
        self.window.mainloop() # Create an event loop
    
    def moveBall(self,dx,dy) :
        
        if(self.ballWithinCanvas()):
            self.canvas.move("circle",dx,dy)
        #else:
            #reset position
            #self.canvas.move("circle",-dx,-dy)

    def ballWithinCanvas(self):
        x0,y0,x1,y1 = self.canvas.coords(self.oval) # x0,y0,x1,y1 of the oval

        print(x0)
        print(y0)
        print(x1)        
        print(y1)        

        #collosion detection
        if (x0 < 10):
            self.canvas.move("circle", 10,0)
            return False
        elif (y0 < 10): 
            self.canvas.move("circle", 0, 10)
            return False
        elif (x1 > self.canvas.winfo_width()-10):
            self.canvas.move("circle",-10,0)
            return False 
        elif (y1 > self.canvas.winfo_height()-10):
            self.canvas.move("circle", 0,-10)
            return False
        
        return True

        # screen coordinates of the canvas should I need them :
        # x, y = (self.canvas.winfo_rootx(), self.canvas.winfo_rooty()) # upper left corner of canvas 
        # width, height = (self.canvas.winfo_width(), self.canvas.winfo_height()) # width and height of canvas
        # xUpLeft, yUpLeft, xDownRight, yDownRight = (x, y, x+width, y+height) # four corners of the canvas
            
        
    def centerWindow(self):
            #Set size of playing area
            Tk_Width = 450
            Tk_Height = 500

            #calculate coordinates to put root window in center of screen
            self.xTopLeft = int(self.window.winfo_screenwidth()/2 - Tk_Width/2)
            self.yTopLeft = int(self.window.winfo_screenheight()/2 - Tk_Height/2)
            print("xTopLeft: " + str(self.xTopLeft)+ ", yTopLeft: " + str(self.yTopLeft))

             # Write following format for center screen
            self.window.geometry("+{}+{}".format(self.xTopLeft, self.yTopLeft))

MoveBall()


