from tkinter import * # Import tkinter



class DisplayGraph(Canvas):
    def __init__(self, container, width = 800, height = 450):
        super().__init__(container, width = width, height = height)
        self.graph = []
        with open('coords.txt','r') as file:
            for line in file:
                  self.graph.append(list(map(int,line.split())))
        self.drawGraph()
        
    def drawGraph(self):  
      size = self.graph.pop(0)[0]
      for i in range(1,size):
         for r in range(len(self.graph[i])):
            u = self.graph[i][0] # could also use 1 instead of pop
            x = self.graph[i][1]
            y = self.graph[i][2] 
            v1 =self.graph[i][3]
            v2 =self.graph[i][4]
         #self.create_line(self.graph[v1][1], self.graph[v1][2],self.graph[v2][1],self.graph[v2][2])
         #print(len(self.graph[i]))
         #self.create_line(self.graph[v1][1], self.graph[v1][2],self.graph[v3][1],self.graph[v3][2])

         #    self.create_line(self.graph[v2][1], self.graph[v2][2],self.graph[v3][1],self.graph[v3][2])
         # if i == 6:
         #    v4 =self.graph[i][6]
         self.create_oval(x - 2, y - 2, x + 2, y + 2, 
                    fill = "black") 
         # Display the name
         self.create_text(x, y - 8, text = str(u))
         self.create_line(self.graph[v1][1], self.graph[v1][2],self.graph[v2][1],self.graph[v2][2])

if __name__ == '__main__':
   window = Tk() # Create a window
   view = DisplayGraph(window,750,410)
   view.pack()
   
   window.mainloop()