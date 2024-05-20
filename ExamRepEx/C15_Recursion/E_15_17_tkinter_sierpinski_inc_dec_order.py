from tkinter import *

class SierpinskiTriangle:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sierpinski Triangle")
        
        self.width = 400
        self.height = 400
        self.canvas = Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()
        
        self.order = 0
        
        # Bind left mouse click to increase order
        self.canvas.bind("<Button-1>", self.increase_order)
        
        # Bind right mouse click to decrease order
        self.canvas.bind("<Button-3>", self.decrease_order)
        
        self.display()
        
        self.window.mainloop()
        
    def display(self):
        self.canvas.delete("line")
        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]
        self.displayTriangles(self.order, p1, p2, p3)
    
    def displayTriangles(self, order, p1, p2, p3):
        if order == 0:
            self.drawLine(p1, p2)
            self.drawLine(p2, p3)
            self.drawLine(p3, p1)
        else:    
            p12 = self.midpoint(p1, p2)
            p23 = self.midpoint(p2, p3)
            p31 = self.midpoint(p3, p1)
    
            self.displayTriangles(order - 1, p1, p12, p31)
            self.displayTriangles(order - 1, p12, p2, p23)
            self.displayTriangles(order - 1, p31, p23, p3)
    
    def drawLine(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")
        
    def midpoint(self, p1, p2):
        p = [0, 0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p
    
    def increase_order(self, event):
        self.order += 1
        self.display()
        
    def decrease_order(self, event):
        if self.order > 0:
            self.order -= 1
            self.display()

SierpinskiTriangle()
