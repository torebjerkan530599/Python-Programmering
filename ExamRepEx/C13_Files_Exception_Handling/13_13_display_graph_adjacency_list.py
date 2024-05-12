from tkinter import * # Import tkinter



class DisplayGraph(Canvas):
    def __init__(self, container, width = 800, height = 450):
        super().__init__(container, width = width, height = height)
        self.graph = []
        self.vertices = {}
        self.edges = {}
        self.size = 0
        with open('coords.txt','r') as file:
            self.size = int(file.readline().strip())
            for line in file:
                parts = line.strip().split()
                u, x, y = map(int, parts[:3])
                self.vertices[u] = (x, y)
                self.edges[u] = list(map(int, parts[3:])) # essentially an adjacency list
                #self.graph.append(list(map(int,line.split())))
        

        self.drawGraph()
        
    def drawGraph(self):
        for vertex, (x,y) in self.vertices.items():
                self.create_oval(x - 2, y - 2, x + 2, y + 2,fill = "black") 
                    # Display the name
                self.create_text(x-8, y - 8, text = str(vertex)) #u
    
        self.drawn_edges = set()  # Set to keep track of already drawn edges
        for start, end_vertices in self.edges.items():
            for end in end_vertices:
                if (start, end) not in self.drawn_edges and (end, start) not in self.drawn_edges: # make sure we draw an edge only once
                    print(start,end)
                    #print(start,end)
                    x1, y1 = self.vertices[start]
                    x2, y2 = self.vertices[end]
                    self.create_line(x1, y1, x2, y2, fill="black")
                    self.drawn_edges.add((start,end))

if __name__ == '__main__':
   window = Tk() # Create a window
   view = DisplayGraph(window,750,410)
   view.pack()
   
   window.mainloop()