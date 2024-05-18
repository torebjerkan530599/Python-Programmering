from pathlib import Path
from tkinter import *
from tkinter.simpledialog import askstring
import tkinter.messagebox

class GraphView(Canvas):
    def __init__(self, graph, master=None):
        super().__init__(master, bg="white", width=400, height=300)
        self.graph = graph
        self.radius = 15
        self.pack()
        self.bind("<Configure>", self.on_resize)
        self.draw_graph()

    def draw_graph(self):
        self.delete("all")
        for u, (x, y, *edges) in enumerate(self.graph):
            self.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill="black")
            self.create_text(x, y, text=str(u), fill="white")
            for v in edges:
                self.create_line(x, y, self.graph[v][0], self.graph[v][1])

    def on_resize(self, event):
        self.draw_graph()


def read_graph(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        graph = []
        for line in lines[1:n+1]:
            parts = list(map(int, line.strip().split()))
            u = parts[0]
            x = parts[1]
            y = parts[2]
            edges = parts[3:]
            graph.append((x, y, *edges))
        return graph


def main():
    root = Tk()
    root.title("Graph Viewer")

    #file_name = askstring("Input", "Enter the file name:")
    file_name = Path(__file__).parent / 'graph_22_20.txt'
    
    if not file_name:
        tkinter.messagebox.showerror("Error", "No file name provided")
        return

    try:
        graph = read_graph(file_name)
        graph_view = GraphView(graph, master=root)
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", "File not found")
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"An error occurred: {e}")

    root.mainloop()


if __name__ == "__main__":
    main()
